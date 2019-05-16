# Search methods

import search

problems = [
        search.GPSProblem('A', 'B', search.romania),
        search.GPSProblem('L', 'A', search.romania),
        search.GPSProblem('S', 'B', search.romania),
        search.GPSProblem('M', 'T', search.romania),
        search.GPSProblem('G', 'V', search.romania)
    ]
for id, problem in enumerate(problems):
    print(" ==== Problem " + str(id) + " Initial: " + str(problem.initial) + " -> " + str(problem.goal) + " ==== \n")
    bfgs_res = search.breadth_first_graph_search(problem)
    print("Breath first graph search : " + str(bfgs_res.node.path()))  # 486
    print("Visited nodes : " + str(bfgs_res.visited_nodes) + "\n")

    dfgs_res = search.depth_first_graph_search(problem)
    print("Depth first graph search : " + str(dfgs_res.node.path()))
    print("Visited nodes : " + str(dfgs_res.visited_nodes) + "\n")

    bbgs_res = search.branch_and_bound_search(problem)
    print("Branch and bound graph search : " + str(bbgs_res.node.path()))  # 374
    print("Visited nodes : " + str(bbgs_res.visited_nodes) + "\n")

    hbbgs_res = search.heuristic_branch_and_bound_search(problem)
    print("Heuristic Branch and bound graph search : " + str(hbbgs_res.node.path()))  # 374
    print("Visited nodes : " + str(hbbgs_res.visited_nodes) + "\n")

