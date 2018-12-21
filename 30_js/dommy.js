/* AstoriaGang (Roster: Shafali, Ahnaf Hasan)
SoftDev1 pd07
K30 -- Sequential Progression III: Season of the Witch
<2018>-<12>-<20>
*/

/**
 * Calculates the nth number in the Fibonacci sequence
 * @param n an integer
 * @returns the nth number in the Fibonacci sequence
 */
var fibonacci = function fib(n) {
    return (n <= 0) ? 0 : ((n == 1) ? 1 : fib(n - 2) + fib(n - 1))
}

//
// DK's Code, taken from QAF
//
// var betterFib = function f(n) {
//     //storing results of subproblems
//     var result = [0, 1];
//     for (var i = 2; i <= n; i++) {
//         result.push(result[i-2] + result[i-1]);
//     }
//     return result[n];
// }

/**
 * Calculates the next number by adding together the two numbers already in list
 * @param n number of the Fibonacci term
 * @returns the **n**th number in the Fibonacci sequence
 */
var bestFib = function(n) {
    let list = document.getElementById('fiblist')
    let first = list.children[list.childElementCount - 1].innerHTML // the last elem on the list
    let second = list.children[list.childElementCount - 2].innerHTML // the second-to-last elem on the list
    return Number(first) + Number(second) // Fib is adding the last to nums so made into O(1)
}

/**
 * Appends the next item to the list of "items".
 */
var listAppend = function() {
    let list = document.getElementById('thelist')
    let children = list.childElementCount // amount of child nodes (num of <li> tags in <ol>)
    let a = document.createElement("li") // make a new tag
    a.innerHTML = `item ${children}`
    list.append(a) // adds the <li> tag to the end of the list
}

/**
 * Changes the header at the top of the page to be the same as the 
 * item hovered over.
 * @param e the MouseEvent (mouseover)
 */
var mouseOver = function(e) {
    console.log(`This is e: ${e['target']}`)
    let thing = e['target'] // e[target] is the item that the MouseEvent is doing stuff on
    console.log(thing.lastChild) // TextNode is a child of the targetted Node, TextNode has the text
    let other = document.getElementById('h')
    other.innerHTML = thing.lastChild.data // child's data is accessed and the header is set as that
}

/**
 * Resets the effects of the _mouseOver_ function.
 */
var reset = function() {
    let h = document.getElementById('h')
    h.innerHTML = "Hello World!"
}

/**
 * Removes the selected item from the list. 
 * @param e the MouseEvent (click)
 */
var removeItem = function(e) {
    let thing = e['target']
    thing.remove()
}

/**
 * Appends the next Fibonacci number to the list. Uses the _fibonacci_ and 
 * the _bestFib_ functions.
 */
var addToFib = function() {
    let l = document.getElementById('fiblist')
    let children = l.childElementCount // num of elems so far in the fibonacci list
    let a = document.createElement("li") // prepare new <li> tag
    if (children < 30) { // normal fib fails around 30 (starts to become slow)
        console.log('using meh fib')
        a.innerHTML = fibonacci(children) // set the text to be the fib num
    }else{ // child count too high for normal fib
        console.log('using great fib')
        a.innerHTML = bestFib(children) // refer to bestFib(n) shown previously
    }
    l.append(a) // add on to the end of the list
}

// -------------------- Function Declarations Above ------------------ //

// ================ Weird Middle Ground of Limbo O_o ================= //

// ~~~~~~~~~~~~~~~~~~~~~~~ Event Listeners Below ~~~~~~~~~~~~~~~~~~~~ //

var b = document.getElementById('b')
b.addEventListener('click', listAppend ) // listen for clicks (sounds like *click*click*click*)

var col = document.getElementById('thelist')

// The name's...Over. 
col.addEventListener('mouseover', mouseOver )

col.addEventListener('mouseout', reset ) // When your mouse is super chill and exits the list

col.addEventListener('click', removeItem ) // listen yet again for clicking (can find a lot of it in a League match)

var fib = document.getElementById('fb')
fib.addEventListener('click', addToFib ) // 1: Ssshh...do you hear that? 2: Hear what? 1: (Deep inhale) Clicks