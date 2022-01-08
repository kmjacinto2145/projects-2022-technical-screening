var assert = require("assert")
// Given an array of numbers, return a new array so that positive and negative
// numbers alternate. You can assume that 0 is a positive number. Within the
// positive and negative numbers, you must keep their relative order. You are
// guaranteed the number of positive and negative numbers will not differ by more
// than 1.

// =====Example 1
// Input: [1, -3, -8, -5, 10]
// Output: [-3, 1, -8, 10, -5]
// Explanation: We have alternated positive and negative numbers. Notice that the
// negative numbers appear in the same relative order (-3, -8, -5) and the positive
// numbers appear in the same order as well (1, 10).

// =====Example 2
// Input: [3, 0, 0, -5, -2]
// Output: [3, -5, 0, -2, 0]
// Explanation: We have alternated positive and negative numbers. Notice they appear
// in the same relative order.

// =====Example 3
// Input: [0, -3, 3, -1, 1, -1]
// Output #1: [0, -3, 3, -1, 1, -1]
// Output #2: [-3, 0, -1, 3, -1, 1]
// Explanation: There are 2 possible answers which satisfy the problem's constraints.
// We can start with either positive or negative

// =====Example 4
// Input numArray: []
// Output numArray: []
// Explanation: Empty array...

const altNumbers = (numArray) => {
    // Initialise arrays of positive and negative numbers
    var positives = [];
    var negatives = [];

    // Populate positive and negative arrays with their corresponding numbers
    // from numArray
    for (var i = 0; i < numArray.length; i++) {
        if (numArray[i] >= 0) {
            positives.push(numArray[i]);
        } else {
            negatives.push(numArray[i]);
        }
    }

    // Initialise sorted array by setting it equal to the numArray
    var sorted = numArray;

    // Replace values in the sorted array with the values from the positives
    // and negatives arrays
    if (positives.length >= negatives.length) {
        // Case 1: start with a positive
        for (var i = 0, j = 0; i < sorted.length; i += 2, j++) {
            sorted[i] = positives[j]
        }

        for (var i = 1, j = 0; i < sorted.length; i += 2, j++) {
            sorted[i] = negatives[j]
        }

    } else {
        // Case 2: start with a negative
        for (var i = 0, j = 0; i < sorted.length; i += 2, j++) {
            sorted[i] = negatives[j]
        }

        for (var i = 1, j = 0; i < sorted.length; i += 2, j++) {
            sorted[i] = positives[j]
        }
    }
    return sorted;
}

module.exports = { altNumbers } // Do not modify this line

// ====================TESTS====================
// Some tests to help you check your progress. Simply run your code with
// node easy.js
// If successful, no output should appear. If unsuccessful, you should see
// assertion errors being thrown.

let array1 = [1, -3, -8, -5, 10]
array1 = altNumbers(array1)
const answer1 = [-3, 1, -8, 10, -5]
for (let i = 0; i < array1.length; i++) {
    assert(array1[i] === answer1[i])
}

let array2 = [3, 0, 0, -5, -2]
array2 = altNumbers(array2)
const answer2 = [3, -5, 0, -2, 0]
for (let i = 0; i < array2.length; i++) {
    assert(array2[i] === answer2[i])
}

let array3 = [0, -3, 3, -1, 1, -1]
array3 = altNumbers(array3)
const answer3a = [0, -3, 3, -1, 1, -1]
const answer3b = [-3, 0, -1, 3, -1, 1]
if (array3[0] === 0) {
    for (let i = 0; i < array3.length; i++) {
        assert(array3[i] === answer3a[i])
    }
} else if (array3[0] == -3) {
    for (let i = 0; i < array3.length; i++) {
        assert(array3[i] === answer3b[i])
    }
} else {
    assert(false)
}

let array4 = []
array4 = altNumbers(array4)
assert(array4.length === 0)
