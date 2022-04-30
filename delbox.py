from itertools import combinations
import pandas as pd

df = pd.read_csv('order.csv', index_col=0)


def delbox(number, capacity, weight_cost):
    """
    :param number: number of existing items
    :param capacity: the capacity of delvery box
    :param weight_cost: list of tuples like: [(weight, cost), (weight, cost), ...]
    :return: tuple like: (best cost, best combination list(contains 1 and 0))
    """
    best_cost = None
    best_combination = []
    # generating combinations by all ways: C by 1 from n, C by 2 from n, ...
    for way in range(number):
        for comb in combinations(weight_cost, way + 1):
            weight = sum([wc[0] for wc in comb])
            cost = sum([wc[1] for wc in comb])
            if (best_cost is None or best_cost < cost) and weight <= capacity:
                best_cost = cost
                best_combination = [0] * number
                for wc in comb:
                    best_combination[weight_cost.index(wc)] = 1
    return best_cost, best_combination


if __name__ == "__main__":
    print("Welcome to Bin Optimization Algorithm")
    print("Order List Retrieved from Database....")
    print(df)
    val = df['val'].tolist()
    wgt = df['wgt'].tolist()
    W = int(input("Enter the maximum capacity of the container in (kg):"))
    n = len(wgt)  # int(input("\nEnter the number of items to be delivered:"))
    # for i in range(n):
    #   print("\nEnter the value & weight of order:", i, " Below")
    #  v = int(input("\nValue : "))
    # wt = int(input("\nWeight : "))
    # val.append(v)
    # wgt.append(wt)

    wc = list(zip(wgt, val))
    #wt = [10, 20, 30]
    y = []
    x, y = delbox(n, W, wc)
    print("\n\nTotal Possible profit:", x)
    print("\nItems include are : ", y)
    df['Possible_in_delbox'] = y
    print("Delivery Order after bin optimization:")
    print(df)
    print("Sucessfully Created delivery order database!!!!")
    df.to_csv('del_order.csv')
