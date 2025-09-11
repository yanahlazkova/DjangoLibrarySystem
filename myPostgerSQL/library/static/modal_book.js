var modal = document.getElementById("myModal");
var form = document.querySelector(".formBook");
var formTitle = document.getElementById("bookModalTitle");
var bookIdField = document.querySelector('input[name="book_id"]');
var submitButton = document.querySelector('input[name="submit"]');

// Функція для відкриття модального вікна
function openModal(bookId) {
    form.reset();
  if (bookId) { // режим редагування
    formTitle.textContent = `Редагування: (id-${bookId})`;
    form.action = `edit_book/${bookId}/`;
    submitButton.value = "Save";
    getDataBook(userId);
    form.style.display = "none";
    form.style.display = "block";
    }
  else {
    console.log('New book')
    formTitle.textContent = "Add new book";
//    form.action = `new_book/`;
//    userIdField.value = '';
    submitButton.value = "Додати";
    form.style.display = "none";
    form.style.display = "block";
    }

  modal.style.display = "block";
}

// Функція для закриття модального вікна
function closeModal() {
  modal.style.display = "none";
}

// Закриття вікна, якщо користувач клацне за межами модального вікна
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

//function getDataBook(userId) {
//    console.log('Edit');
//
//    fetch(`get_book/${userId}/`)
//        .then(response => {
//            // Перевіряємо, чи був запит успішним
//            if (!response.ok) {
//                // Якщо відповідь не 200 OK, викидаємо помилку
//                // Щоб отримати більш детальні дані про помилку, парсимо відповідь
//                return response.json().
//                    then(errorData => {
//                        throw new Error(errorData.error || "Невідома помилка мережі");
//                });
//            }
//            return response.json();
//        })
//        .then(data => {
//            if (data.success && data.user) {
//                const user = data.user;
////                formTitle.textContent = "Редагування користувача";
//                userIdField.value = userId;
////                form.action = `edit_user/${userId}/`;
//                formEdit.querySelector('input[name="id"]').value = user.id;
//                formEdit.querySelector('input[name="firstname"]').value = user.firstname;
//                formEdit.querySelector('input[name="lastname"]').value = user.lastname;
//                formEdit.querySelector('input[name="age"]').value = user.age;
//                formEdit.querySelector('input[name="email"]').value = user.email;
//                formEdit.querySelector('input[name="login"]').value = user.login;
//                formEdit.querySelector('input[name="password"]').value = user.password;
//                formEdit.querySelector('input[name="phone"]').value = user.phone;
//                formEdit.querySelector('input[type="submit"]').value = 'Save';
//            } else {
//                alert(`Помилка: ${data.error}`);
//            }
//        })
//        .catch(error => alert(`Помилка fetching user, ${error}.`));
//    }
