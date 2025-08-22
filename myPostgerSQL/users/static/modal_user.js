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

function delUser(userId) {
    if (!confirm(`Видалити користувача з id '${userId}' ?`)) {
        return;
    }

    fetch(`delete_user/${userId}/`, {
        method: "DELETE",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "X-Requested-With": "XMLHttpRequest"
        }
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            alert(`Користувача з email ${result.email} було видалено.`);
            // опційно: видаляємо рядок із таблиці
            const tr_id = `row-${userId}`
            const row = document.querySelector(`tr[id="${tr_id}"]`);
            if (row) {
              row.remove();
              console.log(`Видалено рядок з id ${tr_id}`)
            }
            else console.log(`Не знайдено рядок p id ${tr_id}`)
        } else {
            alert(`Помилка: ${result.error}`);
        }
    })
    .catch(error => console.error("Помилка fetching user:", error));
}


// функція для отримання CSRF токена з cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// Функції модального вікна для редагування даних користувача
//var editModal = document.getElementById("editModal");

function openEditModal(userId) {
    console.log('Edit modal')
    getDataUser(userId)
}

function getDataUser(userId) {
    fetch(`/get_user/${userId}/`)
        .then(response => {
            // Перевіряємо, чи був запит успішним
            if (!response.ok) {
                // Якщо відповідь не 200 OK, викидаємо помилку
                // Щоб отримати більш детальні дані про помилку, парсимо відповідь
                return response.json().then(errorData => {
                    throw new Error(errorData.error || "Невідома помилка мережі");
                });
            }
            return response.json();
        })
        .then(user => {
            // Отримали дані користувача у форматі JSON
            const form = document.querySelector('#editModal form'); // Або будь-яка інша форма, що ви використовуєте для редагування

            if (form && user) {
                const form = document.getElementById('formUser');
                document.getElementById('legend').innerText = data.id;
                if (form) {
                    form.querySelector('input[name="firstname"]').value = data.firstname;
                    form.querySelector('input[name="lastname"]').value = data.lastname;
                    form.querySelector('input[name="age"]').value = data.age;
                    form.querySelector('input[name="email"]').value = data.email;
                    form.querySelector('input[name="login"]').value = data.login;
                    form.querySelector('input[name="password"]').value = data.password;
                    form.querySelector('input[name="phone"]').value = data.phone;
                }
                form.action = `/edit_user/${userId}`;
                openModal()
        })
        .catch(error => alert(`Помилка fetching user, ${error}.`))
}

// Функции, которые будут вызываться из второго модального окна
function firstAction() {
  alert('Выполнено первое действие!');
  closeSecondModal();
}

function secondAction() {
  alert('Выполнено второе действие!');
  closeSecondModal();
}

//function openEditModal() {
//  editModal.style.display = "block";
//}
//
//function closeEditModal() {
//  editModal.style.display = "none";
//}
