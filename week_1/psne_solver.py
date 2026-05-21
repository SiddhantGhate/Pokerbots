def solve_psne(p1_matrix, p2_matrix) :
    n = len(p1_matrix)
    m = len(p1_matrix[0])
    ans = []
    for i in range(n) :
        for j in range(m) :
            p1_points = p1_matrix[i][j]
            p2_points = p2_matrix[i][j]

            p1_best_response = True
            p2_best_response = True
            for k in range(n) :
                if p1_matrix[k][j] > p1_points :
                    p1_best_response = False
                    break
            for k in range(m) :
                if p2_matrix[i][k] > p2_points :
                    p2_best_response = False
                    break
            if p1_best_response and p2_best_response :
                ans.append((i, j))
    return ans