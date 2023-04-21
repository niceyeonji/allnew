// function isPrime(num) {
//   if (num === 1) return false;
//   for (let i = 2; i < num; i++) {
//     if (num % i === 0) return false;
//   }
//   return true;
// }

// onmessage = function (e) {
//   const val = e.data.val;
//   let result = isPrime(val);
//   postMessage(result);
// };

onmessage = function (e) {
  let output = 0;
  let input = parseInt(e.data.input);
  let i = 2;
  while (i <= input) {
    if (input % i == 0) break;
    else i++;
  }
  output = input;
  output += input == i ? ' is Prime Number.' : ' is not Prime Number.';
  postMessage(output);
};

// function Prime(num) {
//   if (num < 2) return false;
//   for (let i = 2; i <= num / 2; i++) {
//     if (num % i == 0) {
//       return false;
//     }
//   }
//   return true;
// }

// self.onmessage = function (e) {
//   // 워커 태스크로부터 전달받은 숫자
//   let number = e.data;

//   // 소수 판별 결과 전송
//   self.postMessage(Prime(number));
// };
