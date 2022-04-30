
def delbox(W, wt, val, n):
    dp = [0 for i in range(W+1)]  # Making the dp array
  
    for i in range(1, n+1):  # taking first i elements
        for w in range(W, 0, -1):  # starting from back,so that we also have data of
                                # previous computation when taking i-1 items
            if wt[i-1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])
  
    return dp[W]  # returning the maximum value of knapsack
  

# Driver Code
if __name__ == "__main__":
        val=[]
        wgt=[]
        W = int(input("Enter the maximum capacity of the container in (kg):"))
        n = int(input("\nEnter the number of items to be delivered:"))
        for i in range(n):
            print("\nEnter the value & weight of order:",i," Below")
            v = int(input("\nValue : "))
            wt = int(input("\nWeight : "))
            val.append(v)
            wgt.append(wt)    
        #wt = [10, 20, 30]		
        x, = delbox(W, wgt, val, n)
        print("\n\nTotal Possible profit:",x)
