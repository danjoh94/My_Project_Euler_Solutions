#!/usr/bin/env python3
# -*- coding: cp1252 -*-
'''
Problem 31: Coin Sum 
https://projecteuler.net/problem=31

Problem definition
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

BY: Daniel Johansson
DATE: 2018/08/20
'''


def coin_sum(n, coins):
    """
    Calculates the coin sum 
    
    Algorithm
       coinsum(n) = Table[n-coin][coin] + Table[n][coins[-1]]
       if n == 1
        return 1
       
    Parameters
    ----------
    n : int
       the value to calculate the coin sum from 
    coins : list
       list of coins that is available

    Returns
    -------
    int
        returns the coin sum

    """
    if(len(coins)<=1):
        return 1
    coin = coins[-1]
    if(coin > n):
        return coin_sum(n,coins[:-1])
    if(coin <= 1):
        return 1
    if(n<=1):
        return 1
    return coin_sum(n,coins[:-1]) + coin_sum(n-coin,coins) 

if __name__ == '__main__':
    print(coin_sum(n=200,coins=[1,2,5,10,20,50,100,200]))





