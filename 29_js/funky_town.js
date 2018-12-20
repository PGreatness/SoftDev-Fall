/* The_Great_Spicy (Roster: Puneet Johal, Ahnaf Hasan)
SoftDev1 pd07
K29 -- Sequential Progression II: Electric Boogaloo
<2018>-<12>-<19>
*/


/**
 * Returns the factorial of the given number.
 * @param n an integer
 * @returns n! the factorial of n
 */
var factorial = function fact(n) {
  return ((n < 2) ? 1 : n * fact(n - 1))
  /**
   * i.e
   * if (n < 2) {
   * return 1
   * }else{
   * return n * fact(n - 1)
   * }
   */
}

/**
 * Calculates the nth number in the Fibonacci sequence
 * @param n an integer
 * @returns the nth number in the Fibonacci sequence
 */
var fibonacci = function fib(n) {
  return (n <= 0) ? 0 : ((n == 1) ? 1 : fib(n - 2) + fib(n - 1))
}

/**
 * Calculates the Greatest Common Denominator(GCD) of the two given numbers
 * @param  a the first number to compare with
 * @param b the second number to compare with
 */
var gcd = function gcd(a,b) {
  var counter = 1
  var current_gcd = 0
  if (Math.max(a,b) != b) {
    gcd(b,a)
  }
  while (counter <=a) {
    if(a % counter == 0 && b % counter == 0) {
      current_gcd = counter
    }
    counter +=1
  }
  return current_gcd
}

/**
 * Chooses a random student from a list of predetermined students. Takes no parameters
 * @returns String representation of a student's name
 */
var randS = function randomStudent() {
  var arr = ["Ahnaf", "Shafali", "Tyler", "Tom", "Matthew", "Jennifer", "Elias", "Dipali", "Sam", "Bro"]
  var randNum = Math.floor(Math.random() * arr.length)
  return arr[randNum]
  //return randNum
}

// <------------ JS Functions Above ----------------------> //
//   ~~~~~~~~~~ Weird Middle Ground O_O ~~~~~~~~~~~~~~~~~ //
// <------------ JS Document Interactiion Below ----------> //


/**
 * Gets factorial of **num**, a user-inputted number. Must be a number.
 */
var fact_n = document.getElementById("fact") // get button for factorial
fact_n.addEventListener('click', function() { // listen for clicks (sounds like *click*click*click*)
  let chosen = document.getElementById("f-result") // this is part of the doc that shows the result
  let val = document.getElementById("f-num").value // this is the value that the user inputs, is number
  console.log(`This is val: ${val}`)
  if (val) { // if val is not an empty string
    chosen.innerHTML = `The factorial of ${val} is: ${factorial(val)}` //change the inner text of the tag that shows the results
  }else{ // empty string passed
    chosen.innerHTML = `Please enter a numeric value` // wah wah :(
  }
  console.log(`fact: ${factorial(val)}`)
})


/**
 * Gets the **n**th number in the Fibonacci sequence. **n** is user-defined.
 * **n** must be a number.
 */
var fibber = document.getElementById("fib") // get button for fibonacci-ing
fibber.addEventListener("click", function() { // listen yet again for clicking (can find a lot of it in a League match)
  let chosen = document.getElementById("fib-result") // this the result <p></p> tag
  let val = document.getElementById("fib-num").value // value is number
  console.log(`This is val: ${val}`)
  if (val) { // val isn't empty
    chosen.innerHTML = `Term ${val} in the Fibonacci sequence is: ${fibonacci(val)}` // change text in <p>...</p> to success string
  }else{ // empty value passed
    chosen.innerHTML = `Please enter a numeric value`
  }
  console.log(`fib: ${fibonacci(val)}`)
})


/**
 * Gets the greatest commmon denominator between **val1** and **val2**. Both **val1**
 * and **val2** are user-defined. **val1** and **val2** must be numbers.
 */
var GCD = document.getElementById("gcd") // get button for finding the GCD
GCD.addEventListener("click", function() { // sshh...the clicks are listening
  let chosen = document.getElementById("gcd-result") // result tag
  let val1 = document.getElementById("gcd-num1").value // first number to do GCD with
  let val2 = document.getElementById("gcd-num2").value // second number to do GCD with
  console.log(`These are vals: ${val1} and ${val2}`)
  if (val1 && val2) { // both must be valid numbers
    chosen.innerHTML = `The greatest common denominator for ${val1} and ${val2} is: ${gcd(val1, val2)}`
  }else{
    chosen.innerHTML = `Please enter numeric values for both`
  }
  console.log(`gcd: ${gcd(val1, val2)}`)
})


/**
 * Gets a random student from a previously defined list of students. 
 */
var rand_student = document.getElementById("rand") // get button for random students
rand_student.addEventListener("click", function() { // 1: Ssshh...do you hear that? 2: Hear what? 1: (Elongated inhale) Clicks
  let chosen = document.getElementById("rand-result") // result tag
  // no value required, it's a randomly chosen student
  let student = randS() 
  chosen.innerHTML = `Wheee! Randomly chosen student was: ${student}` // change result tag to have chosen student
  console.log(`Chosen student: ${student}`)
})