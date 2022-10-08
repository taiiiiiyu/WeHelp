// 1.
function calculate(min, max, step) {
  sum = 0;
  i = min;
  while (i <= max) {
    sum += i;
    i = i + step;
  }
  console.log(sum);
}
calculate(1, 3, 1);
calculate(4, 8, 2);
calculate(-1, 2, 2);

// 2
function avg(data) {
  salaryAll = 0;
  for (let i = 0; i < data.employees.length; i++) {
    let obj = data.employees[i];
    if (!obj.manager) {
      sum += obj.salary;
    }
  }
  console.log(sum);
}

avg({
  employees: [
    {
      name: "John",
      salary: 30000,
      manager: false,
    },
    {
      name: "Bob",
      salary: 60000,
      manager: true,
    },
    {
      name: "Jenny",
      salary: 50000,
      manager: false,
    },
    {
      name: "Tony",
      salary: 40000,
      manager: false,
    },
  ],
});

//3
function func(a) {
  return function (b, c) {
    return console.log(a + b * c);
  };
}
func(2)(3, 4);
func(5)(1, -5);
func(-3)(2, 9);

// 4
function maxProduct(nums) {
  let max = nums[0] * nums[1];
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      const num = nums[i] * nums[j];
      if (num > max && nums[i] != nums[j]) {
        max = num;
      }
    }
  }
  console.log(max);
}
maxProduct([5, 20, 2, 6]);
maxProduct([10, -20, 0, 3]);
maxProduct([10, -20, 0, -3]);
maxProduct([-1, 2]);
maxProduct([-1, 0, 2]);
maxProduct([5, -1, -2, 0]);
maxProduct([-5, -2]);

// 5
function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      let num1 = nums[i];
      let num2 = nums[j];
      if (num1 + num2 == target) {
        return [i, j];
      }
    }
  }
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result);

//6
function maxZeros(nums) {
  let max = 0;
  let sum = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] == 0) {
      sum += 1;
    } else {
      sum = 0;
    }
    if (sum > max) {
      max = sum;
    }
  }
  console.log(max);
}
maxZeros([0, 1, 0, 0]);
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]);
maxZeros([1, 1, 1, 1, 1]);
maxZeros([0, 0, 0, 1, 1]);
