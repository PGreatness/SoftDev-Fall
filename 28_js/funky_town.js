/* AstoriaGang (Roster: Shafali Gupta, Ahnaf Hasan)
SoftDev1 pd07
K28 -- Sequential Progression
<2018>-<12>-<18>
*/

/**
 * Returns the factorial of the given number.
 * @param n an integer
 * @returns n! the factorial of n
 */
var factorial = function fact(n) {
  if(n<2){
    return 1;
  }
  else{
    return fact(n-1);
  }
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
