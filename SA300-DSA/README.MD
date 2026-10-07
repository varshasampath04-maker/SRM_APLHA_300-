# Day 1 — Two Sum

## Primary: Two Sum

### Approach
Use a hashmap to store each value and its index while traversing the array.
For every element, calculate the required value and check whether it was already seen.

### Time Complexity
O(n)

### Space Complexity
O(n)

### Edge Case
I initially missed the case where no two numbers add up to the target, so the function should return an empty list.

## Variant 1: Two Sum II

Approach: Use a hashmap to store the values and their indices, then check whether the required complement has already been seen.

## Variant 2: 3Sum

Approach: Fix one number and reduce the remaining problem to Two Sum using a set of previously seen values.

## Variant 3: 3Sum Closest

Approach: Fix two numbers and use a set to check for the required third value, updating the closest sum found.

## Variant 4: 4Sum

Approach: Fix two numbers and reduce the remaining problem to Two Sum using a set for previously seen values.