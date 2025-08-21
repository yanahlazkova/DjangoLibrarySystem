var modal = document.getElementById("myModal");

// Функція для відкриття модального вікна
function openModal() {
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
  if (event.target == editModal) {
    secondModal.style.display = "none";
  }
}


function autofill() {
    const form = document.getElementById('formUser');
    if (form) {
        const fakeData = {
            firstname: faker.person.firstName(),
            lastname: faker.person.lastName(),
            age: faker.number.int({ min: 18, max: 90 }),
            email: faker.internet.email(),
            phone: faker.phone.number({ style: 'international' }),
        };

        form.querySelector('input[name="firstname"]').value = fakeData.firstname;
        form.querySelector('input[name="lastname"]').value = fakeData.lastname;
        form.querySelector('input[name="age"]').value = fakeData.age;
        form.querySelector('input[name="email"]').value = fakeData.email;
        form.querySelector('input[name="login"]').value = fakeData.login;
        form.querySelector('input[name="password"]').value = fakeData.password;
        form.querySelector('input[name="phone"]').value = fakeData.phone;
    }
}


// Функції модального вікна для редагування даних користувача
//var editModal = document.getElementById("editModal");

function delUser(userId) {
    console.log('delUser')
    fetch(`/deleted-user/${userId}/`)
        .then(response => {
//            if (!response.ok) {
//                // Если ответ не OK, обрабатываем ошибку от сервера
//                return response.json().then(errorData => {
//                    throw new Error(errorData.error || "Помилка мережі");
//                });
            alert(`Deleted user with id ${userId`)
            }
//            return response.json();
        })

        .catch(error => alert(error));//console.error("Error fetching user:", error));
}

//function openEditModal() {
//  editModal.style.display = "block";
//}
//
//function closeEditModal() {
//  editModal.style.display = "none";
//}
