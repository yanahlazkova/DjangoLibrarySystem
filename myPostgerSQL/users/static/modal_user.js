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
//var editModal = document.getElementById("editModal");//function openEditModal() {


//  editModal.style.display = "block";
//}
//
//function closeEditModal() {
//  editModal.style.display = "none";
//}
