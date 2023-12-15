const file1 = document.getElementById('input1');
const filebutton1 = document.getElementById('file1-button');

file1.addEventListener('change', function(){
  filebutton1.textContent = this.files[0].name;
})

const file2 = document.getElementById('input2');
const filebutton2 = document.getElementById('file2-button');

file2.addEventListener('change', function(){
  filebutton2.textContent = this.files[0].name;
})

const file3 = document.getElementById('input3');
const filebutton3 = document.getElementById('file3-button');

file3.addEventListener('change', function(){
  filebutton3.textContent = this.files[0].name;
})