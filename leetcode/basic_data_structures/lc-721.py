from typing import List

# -------- initial try -- # ! wrong approach
# only passed 25 / 50, missed some edge cases
# account_dict: key - name, value - a set of index
# iterate over accounts
# for each account, if name is in the keys:
#   for all indices of this name
#   > if the set(emails of name) intersect set(emails of index's name) is not empty:
#     modify accounts[index] to make the email of it contains the union of 2 sets above
#     remove account (can use a mark)
#   > if the set is empty
#     add the index to dict[key]
# sort all the emails
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_dict = {}

        for i in range(len(accounts)):
            # print('---- index: ', i)
            namei = accounts[i][0]
            if not account_dict.get(accounts[i][0]):
                accounts[i] = [accounts[i][0]] + list(set(accounts[i][1:]))
                account_dict[namei] = [i]
                continue

            email_set_i = set(accounts[i][1:])
            is_account_duplicated = False
            for idx in account_dict[namei]:
                email_set_idx = set(accounts[idx][1:])
                # print('email_set_idx {}:'.format(idx), email_set_idx)
                # print('email_set_i {}'.format(i), email_set_i)
                if email_set_i & email_set_idx:
                    accounts[idx] = [accounts[idx][0]] + list(email_set_i | email_set_idx)
                    # print('accounts[idx]:', accounts[idx])
                    accounts[i][0] = None 
                    # print('accounts {} removed'.format(i))
                    is_account_duplicated = True
                    break
                    
            
            if not is_account_duplicated:
                accounts[i] = [accounts[i][0]] + list(set(accounts[i][1:]))
                account_dict[namei].append(i)


        accounts = [[acc[0]] + sorted(acc[1:]) for acc in accounts if acc[0]]

        return accounts
    

# use dfs
# emails_dict: key - emails, value - list of users it belongs
# for each user, add all the accounts its emails belongs to, dfs their emails until no more accounts can be added:
# dfs: given an account, return null
#   add all the emails it contains
#   mark this account as visited
#   dfs all emails' users not visited yet
# the strikethroughed parts are the initial mistakes you did when writing the code,
# // like this
# AC
class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails_dict = {}
        for i in range(len(accounts)):
            for em in accounts[i][1:]:
                # cannot use the traditional get approach here, since
                # for set, add will return None and can only modify the original set # *
                if em not in emails_dict: 
                    # // emails_dict[em] = set() 
                    # // emails_dict[em] = set(i) 
                    emails_dict[em] = set([i]) 
                else:
                    emails_dict[em].add(i)

        visited = [False] * len(accounts)

        def dfs(acc_idx: int):
            emails = set()
            visited[acc_idx] = True

            for em in accounts[acc_idx][1:]:
                # // emails.add(emails)
                emails.add(em)
                for master_id in emails_dict[em]:
                    if visited[master_id]:
                        continue
                    # // emails = emails | dfs(master)
                    emails = emails | dfs(master_id)
            
            # // no return initially
            return emails
        
        ans = []
        for i in range(len(accounts)):
            if not visited[i]:
                ans.append([accounts[i][0]] + sorted(list(dfs(i))))

        return ans


# use disjoint set data structure
# start to AC - 30:13
# AC
class Solution3:
    class DJSet():
        def __init__(self, n):
            self.nodes = list(range(n))

        # return the root of node nid
        # // def find_root(nid) -> int:
        def find_root(self, nid) -> int:
            if self.nodes[nid] != nid:
                self.nodes[nid] = self.find_root(self.nodes[nid])
            
            return self.nodes[nid]

        # make 2 related nodes have the same root
        # // def union_nodes(nd1, nd2):
        def union_nodes(self, nd1, nd2):
            rt1 = self.find_root(nd1)
            rt2 = self.find_root(nd2)
            self.nodes[rt2] = rt1
            # modifies all children of rt2 to be rt1 as well
            # (but it seems that even this is not enough, because later on the root
            # of rt1 can change, but the children of rt1 are not aware of it
            self.find_root(nd2)


    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # // email_dic = dict{}
        # // name_dic = dict{}
        # the names of these 2 can be better
        # like in official .cn solution, the names are emailtoindex and emailtoname
        email_dic = dict()
        name_dic = dict()
        email_count = 0

        for acc in accounts:
            for em in acc[1:]:
                if em not in email_dic:
                    email_dic[em] = email_count
                    email_count += 1
                    name_dic[em] = acc[0]

        dj_set = self.DJSet(len(email_dic))

        for acc in accounts:
            em0 = acc[1]
            for em in acc[2:]:
                # you often made this mistake # *
                # // dj_set.union_nodes(email_dic(em0), email_dic(em))
                # email_dic[em0] better evaluated outside the loop so you do not have to query it many times # *
                dj_set.union_nodes(email_dic[em0], email_dic[em])
        
        # better first use a dictionary to avoid too many empty lists # *
        ans = [[] for i in range(len(email_dic))]

        for em, idx in email_dic.items():
            # this is wrong since the union_node()'s root modification is not enough (see union_nodes() explanation)
            # // root = dj_set.nodes[idx]
            root = dj_set.find_root(idx)
            ans[root].append(em)

        # you wrote email instead emails
        # // ans = [ [name_dic[email[0]]] + sorted(emails) for emails in ans if emails ]
        ans = [ [name_dic[emails[0]]] + sorted(emails) for emails in ans if emails ]

        return ans
