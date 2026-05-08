class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix)-1

        while u <= d:
            mid_u_d = (u + d) // 2
            l, r = 0, len(matrix[0])-1
            while l <= r:
                mid_l_r = (l + r) // 2

                if matrix[mid_u_d][mid_l_r] > target:
                    r = mid_l_r -1
                elif matrix[mid_u_d][mid_l_r] < target:
                    l = mid_l_r +1
                elif matrix[mid_u_d][mid_l_r] == target:
                    return True

            if matrix[mid_u_d][0] > target:
                d = mid_u_d -1
            else:
                u = mid_u_d +1
        
        return False
