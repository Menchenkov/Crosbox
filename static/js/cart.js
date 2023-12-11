// $('.minus-btn').on('click', function (e) {
//     e.preventDefault();
//     let $this = $(this);
//     let $input = $this.closest('div').find('input');
//     let value = parseInt($input.val());
//
//     if (value &gt; 1) {
//         value = value - 1;
//     } else {
//         value = 0;
//     }
//
//     $input.val(value);
//
// });
//
// $('.plus-btn').on('click', function (e) {
//     e.preventDefault();
//     let $this = $(this);
//     let $input = $this.closest('div').find('input');
//     let value = parseInt($input.val());
//
//     if (value &lt; 100) {
//         value = value + 1;
//     } else {
//         value = 100;
//     }
//     $input.val(value);
// });

var quantity = 1; // начальное значение количества товара

function increaseQuantity() {
  quantity++; // увеличиваем количество на 1
  document.getElementById("quantity").innerHTML = quantity; // обновляем значение в элементе HTML
}

function decreaseQuantity() {
  if (quantity > 1) { // проверяем, что количество больше 1
    quantity--; // уменьшаем количество на 1
    document.getElementById("quantity").innerHTML = quantity; // обновляем значение в элементе HTML
  }
}


