class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split('/')
        st = []
        
        for i in range(len(path)):

            if path[i]:

                if st and path[i] == ".." :

                    st.pop()

                elif path[i] != "." and path[i] != "..":

                    st.append(path[i])

        
        st = '/' + '/'.join(st)
        return st




        