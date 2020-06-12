function inchToCentimeter(inch) {
	var centimeter = inch * 2.54; // 1 inch = 2.54cm
	return centimeter;			 // cm로 계산한 결괏값 돌려주기
}

var result1 = inchToCentimeter(2);  // 2 inch를 cm로 바꾼 값
var result2 = inchToCentimeter(3);  // 3 inch를 cm로 바꾼 값

console.log(result1);
console.log(result2);
console.log(inchToCentimeter(1) + inchToCentimeter(5)); 