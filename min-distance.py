# 最短路径问题

# 一般最短路问题可以通过 BFS 求解，动态规划也是在 BFS 基础上优化

# Floyd, 动态规划 => 任一两个点最短路径问题
# Dijkstra, 贪心 => 某个点出发到其它点的最短路径问题

# Bellman Floyd, 动态规划 => 有边数限制的最短路问题，「限制最多经过不超过 k 个点」
# Bellman-Ford 算法和 Dijkstra 算法都是可以解决单源最短路径的算法，
# 一个实现的很好的 Dijkstra 算法比 Bellman-Ford 算法的运行时间要低，
# 但dijkstra算法无法解决存在负权环的图的单源最短路问题
# （因为dijkstra算法每循环一次，确定一条到某个顶点的最短路，
# 之所以能确定，是因为每条边都是正值，
# 若到达其他顶点的最短路经过该顶点，则最短路总权值会更大）。


# https://leetcode-cn.com/problems/01-matrix/
# https://leetcode-cn.com/problems/network-delay-time/
