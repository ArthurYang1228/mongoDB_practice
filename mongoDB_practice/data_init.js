doc_arr = [];
category_set = ["A","B","C","D"]
var category_index = 0;
var amount = 0;
for(i = 0; i<1000; i++){
  category_index  = Math.floor(Math.random() * category_set.length);
  amount = Math.floor(Math.random() * 10)+1;

  doc_arr.push({"category":category_set[category_index],
  "amount":amount
  })
}


 db.grade_stat.insertMany( doc_arr );