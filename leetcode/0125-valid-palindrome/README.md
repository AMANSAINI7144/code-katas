# 125- Valid Palindrome (_LeetCode_)

> Given a string `s`, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases

A palindrome is a string that is "read" the same forwards and backwards. The
proverberial example of a palindrome is "racecar".

This particular problem has two stipulations:

- `considering only alphanumeric characters` — we ignore all non-alphas
- `...and ignoring cases` — `a` == `A`, `b` == `B`, etc.

Edge cases for the test harness are likely why this problem is so terribly
received on LeetCode. Alas, we will have to deal with this.

- - -

The interesting thing about this problem is that it doesn't necessarily
require a typical comparison sort <sup id="a1">[\[1\]](#f1)</sup> like how some
problems ask.

The `0`s, `1`s and `2`s in this particular array are indistinguishable from one
another. As a result, the only value an element has in this array is whether
it's a `0`, `1`, or `2`. This is in contrast to comparison-based algorithms
where elements are compared using a key, but it doesn't imply that the elements
are equal. But equality is not sameness.

Using this idea, we can subvert how most sorting algorithms operate and instead
use a particular instance of
[bucket sort](https://en.wikipedia.org/wiki/Bucket_sort) known as
"counting sort".<sup id="a2">[\[2\]](#2)</sup>, where instead of comparing
elements, we literally just count them.

## Algorithm

1. Count the number of zeroes into `num_zeroes`

2. Count the number of ones into `num_ones`

3. Count the number of twos into `num_twos`

4. Write `num_zeroes` zeroes into the array, starting at index `0`

5. Write `num_ones` ones into the array, after the last `0`

6. Write `num_twos` twos into the array, after the last `1`

This algorithm runs in Θ(_n_) time, requiring one pass over the initial array,
and one final pass to rewrite the elements of the array. This algorithm, like
counting sort, only works because we can enumerate the entirety of an element's
value in an indistinguishable way.

## Notes

<b id="f1">1. </b> [^](#a1) A sort that involves comparing elements relative
to each other, which is mathematically bounded to Θ(_n log n_). See
[Wikpedia](https://en.wikipedia.org/wiki/Comparison_sort).

<b id="f2">2. </b> [^](#a2) Also known as histogram sort; in both cases we
deal with bins/"buckets" and distribute elements into them.
