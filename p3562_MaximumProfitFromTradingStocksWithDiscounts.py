from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # Build adjacency list (tree structure)
        # Convert 1-based hierarchy to 0-based for internal indexing
        children = [[] for _ in range(n)]
        for u, v in hierarchy:
            children[u - 1].append(v - 1)
        
        # Helper: Merges two dictionaries {cost: profit}
        # Similar to combining two groups of items in a Knapsack problem
        def merge_knapsacks(d1, d2):
            new_dp = {}
            # Convert to lists to iterate efficiently
            items1 = list(d1.items())
            items2 = list(d2.items())
            
            for c1, p1 in items1:
                for c2, p2 in items2:
                    new_cost = c1 + c2
                    if new_cost <= budget:
                        new_profit = p1 + p2
                        # Keep the max profit for this specific cost
                        if new_profit > new_dp.get(new_cost, -float('inf')):
                            new_dp[new_cost] = new_profit
            return new_dp

        # Helper: Combines two choices (e.g., 'Buy Node' vs 'Skip Node')
        # Takes the best profit for each cost found in either dictionary
        def combine_choices(d1, d2):
            res = d1.copy()
            for c, p in d2.items():
                if p > res.get(c, -1):
                    res[c] = p
            return res

        # Post-order DFS
        def dfs(u):
            # Calculate costs and profits for current node u
            price_full = present[u]
            profit_full = future[u] - price_full
            
            price_half = present[u] // 2
            profit_half = future[u] - price_half
            
            # --- Initialize States for Node u ---
            
            # 1. Skip u: Cost 0, Profit 0
            dp_skip = {0: 0}
            
            # 2. Buy u (Full Price): Valid if price fits in budget
            dp_buy_full = {}
            if price_full <= budget:
                dp_buy_full[price_full] = profit_full
                
            # 3. Buy u (Half Price): Valid only if parent bought
            dp_buy_half = {}
            if price_half <= budget:
                dp_buy_half[price_half] = profit_half
            
            # --- Merge Children ---
            for v in children[u]:
                # Recursively get results from child
                # child_res_0: Best profits if WE (u) don't buy
                # child_res_1: Best profits if WE (u) do buy
                child_res_0, child_res_1 = dfs(v)
                
                # If we skipped u, our children see "Parent Not Bought"
                dp_skip = merge_knapsacks(dp_skip, child_res_0)
                
                # If we bought u (either full or half), our children see "Parent Bought"
                dp_buy_full = merge_knapsacks(dp_buy_full, child_res_1)
                dp_buy_half = merge_knapsacks(dp_buy_half, child_res_1)
                
            # --- Finalize Return Values for u ---
            
            # Return Case 0: u's parent did NOT buy
            # u can either Skip or Buy Full
            res_parent_no_buy = combine_choices(dp_skip, dp_buy_full)
            
            # Return Case 1: u's parent DID buy
            # u can either Skip or Buy Half
            res_parent_buy = combine_choices(dp_skip, dp_buy_half)
            
            return res_parent_no_buy, res_parent_buy

        # Root is 0 (Input ID 1). The CEO has no boss, so we look at the "Parent No Buy" case.
        final_dp, _ = dfs(0)
        print(final_dp)
        
        # The answer is the maximum profit found in the final DP table
        # Use max(0, ...) to handle edge cases where no profitable trade exists
        return max(0, max(final_dp.values()))
