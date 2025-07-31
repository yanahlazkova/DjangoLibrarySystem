import * as webStorage from "./Coockies_LocalStorage";
import * as dataFake from "./dataFake";

// setCookies();
let defaultTextColor = "green"; // колір тексту позамовчуваню

// const radioBlue = document.getElementById("blue");
// const radioGreen = document.getElementById("green");

// події при зміні кольору текстру Radio
const radios = document.querySelectorAll("input[type=radio][name=text_color]");
radios.forEach((radio) => {
  radio.addEventListener("change", (event) => {
    // додати колір у файл cookies
    document.cookie = event.target.name + "=" + event.target.value;
    // змінити колір
    setTextColor(event.target.value);
  });
});

// Створення h1
const h1 = document.createElement("h1");
h1.innerText = "Library system";
// document.body.append(h1);

// отримаємо елемент по ID
// I - варіант
const table = document.body.querySelectorAll("table")[0]; // firstElementChild.nextElementSibling.firstElementChild;
// console.log(table.tagName);

// розміщення h1 в горі сторінки
const divContainer = document.body.getElementsByClassName("container")[0];
table.before(h1, divContainer);

// дії після завантаження всіх елементів на сторінку
document.addEventListener("DOMContentLoaded", () => {
  // встановлення кольору тексту
  setTextColor();
  // заповнити поля останніми даними, які не були збережені минулого разу
  const noSavedData = webStorage.getLocalStorage("no_saved_data");
  if (noSavedData) {
    fillData(JSON.parse(noSavedData));
  }
  return true;
});

function setTextColor() {
  const col = webStorage.getCookiesColor("text_color");
  const textColor = col || defaultTextColor;
  console.log(textColor);
  divContainer.style.color = textColor;
  document.querySelector(`[value=${textColor}]`).checked = true;
}

// II - варіант
// const table = document.getElementById('table');

// I варіант
// const tableRows = table.rows;
// console.log(tableRows);
// for (tr of tableRows) {
//     const tableCells = tr.cells;
//     for (td of tableCells) {
//         td.innerText = `${td.cellIndex + 1}:${tr.rowIndex + 1}`;
//         console.log(tableCells[td.cellIndex]);
//         if (td.cellIndex == tr.rowIndex)  td.style.backgroundColor = 'red';
//     }

// }

// II варіант
for (let i = 0; i < table.rows.length; i++) {
  const row = table.rows[i];
  row.cells[i].innerText = `${i + 1}:${i + 1}`;
  row.cells[i].style.backgroundColor = "red";
}

// table - ссылка на элемент с id="table"
table.style.backgroundColor = "blue";
table.style.color = "green";

// внутри id="bg-grey" есть дефис, так что такой id не может служить именем переменной
// ...но мы можем обратиться к нему через квадратные скобки: window['bg-grey']
// window['bg-grey'].style.backgroundColor = 'grey';

const links = document.querySelectorAll('[href*="://"]');
links.forEach((link) =>
  link.getAttribute("href").startsWith("http://internal.com")
    ? null
    : (link.style.color = "orange")
);

// змінемо данні форми AddBook вручну

// const formAddBook = document.querySelector('form.AddBook');
const formAddBook = document.forms.addbook;
formAddBook.onsubmit = save; // toSaveData;

// Title
const labelBookTitle = formAddBook.querySelector('label[for="bTitle"]');
labelBookTitle.innerHTML = "Book Title:";

const inputBookTitle = formAddBook.querySelector('input[id="bTitle"]');
inputBookTitle.setAttribute("placeholder", "Title of the book..");
inputBookTitle.className = "";
// inputBookTitle.required = true;
inputBookTitle.addEventListener("blur", checkValue);

// Author
const labelBookAuthor = formAddBook.querySelector('label[for="author"');
labelBookAuthor.innerHTML = "Author:";

const inputBookAuthor = formAddBook.querySelector("#author");
inputBookAuthor.setAttribute("placeholder", "Author..");
// inputBookAuthor.required = true;
inputBookAuthor.addEventListener("blur", checkValue); // потеря фокусу

// Видалимо div з тегом area
inputBookAuthor.parentElement.parentElement.nextElementSibling.nextElementSibling.remove(); //setAttribute('hidden', 'true');

// знайдемо Country
// та змінемо його на Gener

const labelBookGenre = formAddBook.querySelector("label[for=country]");
const divBookGenre = labelBookGenre.parentElement.parentElement;
labelBookGenre.setAttribute("for", "genre");
labelBookGenre.innerHTML = "Genre:";

const selectBookGenre = formAddBook.querySelector("#country");
selectBookGenre.id = "genre";
selectBookGenre.name = "genre";
// selectBookGenre.required = true;
// listDate.push(selectBookGenre);

const optionBookGenreFantasy = selectBookGenre.firstElementChild;
optionBookGenreFantasy.setAttribute("value", "fantasy");
optionBookGenreFantasy.innerHTML = "Fantasy";

const optionBookGenreDetective = optionBookGenreFantasy.nextElementSibling;
optionBookGenreDetective.setAttribute("value", "detective");
optionBookGenreDetective.innerHTML = "Detective";

const optionBookGenreThriller = optionBookGenreDetective.nextElementSibling;
optionBookGenreThriller.setAttribute("value", "thriller");
optionBookGenreThriller.innerHTML = "Thriller";

const optionBookGenreHorror = document.createElement("option");
optionBookGenreHorror.setAttribute("value", "horror");
optionBookGenreHorror.innerHTML = "Horror";
selectBookGenre.append(optionBookGenreHorror);

const optionBook = document.createElement("option");
optionBook.defaultSelected = true;
optionBook.value = ""; //'empty';
optionBook.innerHTML = "";
selectBookGenre.prepend(optionBook);

// створимо div для Year:
const divBookYear = document.createElement("div");
divBookYear.setAttribute("class", "row");
// divBookYear.style.backgroundColor = 'blue';
// divBookYear.style.height = '50px';
divBookGenre.before(divBookYear);

const labelBookYear = document.createElement("label");
labelBookYear.setAttribute("for", "year");
labelBookYear.innerHTML = "Year:";
divBookYear.appendChild(labelBookYear);

const selectBookYear = document.createElement("select");
selectBookYear.id = "byear";
selectBookYear.name = "byear";
const option = document.createElement("option");
option.value = option.innerHTML = "";
selectBookYear.append(option);
for (let optionYear = 2025; optionYear > 1950; optionYear--) {
  const option = document.createElement("option");
  // option.setAttribute('value', optionYear);
  option.innerHTML = option.value = optionYear;
  selectBookYear.append(option);
}

divBookYear.append(selectBookYear);
inputBookAuthor.parentElement.parentElement.after(divBookYear);
// selectBookYear.required = true;
// listDate.push(selectBookYear);

// отримаємо div кнопки Submit та розмістимо внизу форми
// const divButtonSubmit = formAddBook.querySelector('input[type="submit"]').parentElement;

// або:
// const divSubmit = formAddBook.lastElementChild;

// Створення div для книг e-book
const divEbook = document.createElement("div");
divEbook.className = "row";
divBookYear.after(divEbook);

const fieldsetEbook = document.createElement("fieldset");
fieldsetEbook.className = "row";
fieldsetEbook.hidden = true;
fieldsetEbook.name = "ebookFieldset";
divEbook.after(fieldsetEbook);

const legendEBook = document.createElement("legend");
legendEBook.innerHTML = "Info e-book:";
fieldsetEbook.append(legendEBook);

const checkboxEbook = document.createElement("input");
checkboxEbook.setAttribute("type", "checkbox");
checkboxEbook.id = "ebook";
checkboxEbook.name = "ebook";
checkboxEbook.checked = false;
checkboxEbook.onchange = isEBook;

// legendEBook.append(checkboxEbook);

const labelEBook = document.createElement("label");
labelEBook.innerHTML = "e-Book";
labelEBook.setAttribute("for", "ebook");
labelEBook.style.marginLeft = "5px";
labelEBook.style.marginTop = "16px";
// labelEBook.onclick = isEBook;
// divCheckboxEBook.append(checkboxEbook, labelEBook);
divEbook.append(checkboxEbook, labelEBook);

const divOpenFile = document.createElement("div");
divOpenFile.hidden = true;
divEbook.append(divOpenFile);

// вибір файлу e-Book
const inputEBookFile = document.createElement("input");
inputEBookFile.id = "ebookfile";
inputEBookFile.name = "ebookfile";
inputEBookFile.type = "file";
inputEBookFile.addEventListener("change", showDataEBook);
inputEBookFile.hidden = true;
divEbook.append(inputEBookFile);

// Кнопка вибору файлу
const labelOpenFile = document.createElement("label");
labelOpenFile.setAttribute("for", "ebookfile");
labelOpenFile.className = "openfile";
labelOpenFile.innerHTML = "Вибрати файл";
// labelOpenFile.hidden = true;

// відображення назви вибраного файлу
const labelFileName = document.createElement("label");
labelFileName.name = "filename";
labelFileName.value = "Нічого не вибрано..";
labelFileName.style.marginLeft = "15px";
labelFileName.style.marginTop = "16px";
labelFileName.style.color = "gray";
// labelFileName.hidden = true;

divOpenFile.append(labelOpenFile, labelFileName);

const preInforEBook = document.createElement("pre");
// preInforEBook.required = checkboxEbook.checked;
legendEBook.after(preInforEBook);

// створення div та кнопки для auto-заповнення полів
const divAutoFill = document.createElement("div");
divAutoFill.className = "row";
formAddBook.prepend(divAutoFill);

// const buttonAuto = formAddBook.querySelector('input[type=submit]').cloneNode(true);// document.createElement('input');
const buttonAuto = document.createElement("button");
buttonAuto.onclick = autoFillData;
buttonAuto.innerHTML = "Auto fill";
buttonAuto.setAttribute("type", "button");
buttonAuto.disabled = true;
divAutoFill.append(buttonAuto);

// checkbox автозаповнення
const divCheckboxAutoFill = document.createElement("div");
// divCheckboxAutoFill.onclick = isAutoFill;
divAutoFill.append(divCheckboxAutoFill);

const checkboxAutoFill = document.createElement("input"); // checkboxEbook.cloneNode(false);
checkboxAutoFill.type = "checkbox";
checkboxAutoFill.id = "autofill";
checkboxAutoFill.name = "autofill";
checkboxAutoFill.onclick = isAutoFill;
checkboxAutoFill.checked = false;
divCheckboxAutoFill.append(checkboxAutoFill);

const labelCheckboxAutoFill = document.createElement("label");
labelCheckboxAutoFill.innerHTML = "Автоматичне заповнення";
labelCheckboxAutoFill.setAttribute("for", "autofill");
labelCheckboxAutoFill.style.marginLeft = "10px";
divCheckboxAutoFill.append(labelCheckboxAutoFill);

// поле ID
const divID = document.createElement("div");
divID.className = "row";

const divLabelID = formAddBook
  .getElementsByClassName("col-25")[0]
  .cloneNode(true);
divLabelID.firstElementChild.innerHTML = "Book-id:";
divLabelID.firstElementChild.setAttribute("for", "id");

const divInputID = formAddBook
  .getElementsByClassName("col-75")[0]
  .cloneNode(true);
const inputID = divInputID.firstElementChild;
// inputID.required = false;
inputID.name = "idbook";
inputID.id = "id";
inputID.setAttribute("style", "width: 200px");
inputID.placeholder = "Enter id..";
const buttonID = document.createElement("button");
buttonID.type = "button";
buttonID.className = "button";
buttonID.setAttribute("style", "margin-top: 0");
buttonID.innerHTML = "set ID";
buttonID.onclick = setID;
inputID.after(buttonID);
divID.append(divLabelID, divInputID);

// розділювач
const hr = document.createElement("hr");
document.forms[0].firstElementChild.after(hr);
hr.after(divID);

// кнопка Submit
const submit = formAddBook.querySelector("input[type=submit]");
submit.value = "Save";

// повідомлення <p>
const divP = document.createElement("div");
divP.className = "row";
const spanMessage = document.createElement("span");
spanMessage.className = "message";
spanMessage.value = "** Заповніть обов'язкові поля";
spanMessage.innerHTML = "** Заповніть обов'язкові поля";
divP.append(spanMessage);
hr.after(divP);

// для кожного з полів встановити дію при зміні даних та встановити доступною кнопку Save
for (let elem of formAddBook.querySelectorAll(
  "#ebookfile, input[type=text], select"
)) {
  elem.onchange = () => {
    if (submit.disabled) {
      submit.disabled = !submit.disabled;
    }
  };
}

// перевірка заповнення полів
function checkValue(e) {
  if (e.target.value != "") {
    e.target.className = "";
    spanMessage.className = "message";
    spanMessage.innerHTML = spanMessage.value;
  }
  return true;
}

// показати/сховати додавання файлу e-Book
function isEBook() {
  // console.log(e.target.checked, !checkboxEbook.checked);
  divOpenFile.hidden = !checkboxEbook.checked;
  // console.log(labelOpenFile.hidden);
  fieldsetEbook.hidden = divOpenFile.hidden;
  preInforEBook.hidden = divOpenFile.hidden;
}

// відображення даних (путь до файлу, ім'я, розмір, формат файлу) eBook
function showDataEBook() {
  if (this.files.length > 0) {
    fieldsetEbook.hidden = false;
    const currentFile = this.files[0];
    const format = currentFile.type.substring(
      currentFile.type.lastIndexOf("/") + 1
    );

    // показати данні обраного файлу e-Book
    const infoEBook =
      `Path:  <span style='color: lightgrey'>${this.value}</span><br>` +
      `Name:  <span style='color: lightgrey'>${currentFile.name}</span><br>` +
      `Size:  <span style='color: lightgrey'>${currentFile.size}</span> bites<br>` +
      `Format:  <span style='color: lightgrey'>${format}</span>`;

    preInforEBook.innerHTML = infoEBook;
    labelFileName.innerHTML = inputEBookFile.value.substring(
      inputEBookFile.value.lastIndexOf("\\") + 1
    );
  } else {
    // labelFileName.innerHTML = "Нічого не вибрано..";
    labelFileName.innerHTML = labelFileName.value;
  }
  return true;
}

// збереження даних форми
function toSaveData(event) {
  event.preventDefault(); // заборона стандартної відправки форми
  // валідація форми
  validateForm()
    .then((message) => {
      spanMessage.className = "message";
      spanMessage.innerHTML = spanMessage.value;
      // додати збережені дані у localStorage (key=saved_data)
      // і видалити з key=no_saved_data
      let noSavedData = JSON.parse(webStorage.getLocalStorage("no_saved_data"));
      let savedData = JSON.parse(webStorage.getLocalStorage("saved_data"));
      if (noSavedData) {
      } else {
        const noSavedData = createObjectForLocalStorage();
        webStorage.setLocalStorage(
          "no_saved_data",
          JSON.stringify(noSavedData)
        );
      }
      if (!savedData) {
        savedData = {};
      }
      // const book = noSavedData.idBook;
      console.log(noSavedData);
      savedData[noSavedData.idBook] = noSavedData;
      webStorage.setLocalStorage("saved_data", savedData);
      webStorage.removeLocalStorage("no_saved_data");
      submit.disabled = true;
      alert(message);
    })
    .catch((errors) => {
      console.log(errors);
      spanMessage.setAttribute("class", "error");
      spanMessage.innerHTML = `** Виділені поля (${errors}шт.) повинні бути заповнені`;
    });
}

function save(event) {
  event.preventDefault();
  const promise = new Promise((resolve, reject) => {
    validateForm()
      .then(
        (result) => {
          console.log("Validate:", result);
          spanMessage.className = "message";
          spanMessage.innerHTML = spanMessage.value;
          const dataBook = createObjectForLocalStorage();
          let savedData = webStorage.getLocalStorage("saved_data");
          !savedData
            ? (savedData = {})
            : (savedData[dataBook.idBook] = dataBook);
          webStorage.setLocalStorage("saved_data", savedData).then(
            (result) => alert,
            (error) => alert
          );
        },
        (error) => console.log("Error", error)
      )
      .finally((result) => {
        confirm("Clear is form?")
          ? console.log("Clearing..")
          : console.log("Editing..");
      });
    return true;
  });
}

// перевірка заповнення обов'язкових полів

// I - спосіб

// function validateForm(e) {
//   // console.log('validate', e);

//   let countInvalidFields = 0;

// // зміна класу незаповнених полів (border color - red)
//   const listDate = formAddBook.querySelectorAll('[required]')
//   // console.log(listData);
//   listData.forEach((field) => {
//     // if (field.value == "") {
//     //   field.className = "error";
//     //   countInvalidFields++;
//     // } else {
//     //   field.className = "";
//     // }

//     console.log(field.name +': ' + field.checkValidity());
//   });
//   if (checkboxEbook.checked & (inputEBookFile.files.length == 0) & !checkboxAutoFill.checked) {
//     inputEBookFile.className = 'error';
//     countInvalidFields++;
//   } else inputEBookFile.className = "";
//   if (countInvalidFields) {
//     // pMassage.hidden = false;
//     pMassage.setAttribute("class", "error");
//     pMassage.innerHTML = `** Marked fields (${countInvalidFields}) must be filled out`;
//   } else {
//     pMassage.className = "message";
//     pMassage.innerHTML = 'Данні передані';
//     submit.disabled = true;
//     inputEBookFile.className = "";
//   }
//   return false;
// }

// II - спосіб (за допомогою Promise)
function validateForm() {
  return new Promise((resolve, reject) => {
    try {
      let errors = 0;
      const listValidateFields = [inputID, inputBookTitle, inputBookAuthor];
      if (checkboxEbook.checked) {
        listValidateFields.push(labelFileName);
      }

      listValidateFields.forEach((field) => {
        if (!validateFieldEmptyValues(field)) errors++;
      });

      if (errors > 0) {
        reject(errors);
      } else {
        resolve("Валідація успішна..");
      }
    } catch (error) {
      reject("Помилка валідації: " + error.message);
    }
  });
}

function validateFieldEmptyValues(field) {
  if (field.name == "filename") {
    return field.innerHTML != field.value;
  } else {
    if (field.value) {
      // console.log('true: ', field.value);
      field.className = "";
      return true;
    } else {
      // console.log('false: ', field.name);
      field.className = "error";
      return false;
    }
  }
}

// const isAutoFill = () => {}

// автозаповнення
function isAutoFill() {
  buttonAuto.disabled = !buttonAuto.disabled;
  submit.disabled = buttonID.disabled = !buttonAuto.disabled;
  spanMessage.className = "message";

  // якщо дані в повідомленні були змінені (тобто при авто заповнені було повідомлення що дані відправлені),
  // щоб не було можливості відправити ті самі данні повторно при знятті галочки Автозаповлення -
  // заблокувати повторне відправлення даних
  if (spanMessage.innerHTML != spanMessage.value) {
    spanMessage.innerHTML = spanMessage.value;
    submit.disabled = true;
  }

  for (let elem of formAddBook.querySelectorAll(
    "#ebook, input[type=text], select"
  )) {
    elem.disabled = !elem.disabled;
    elem.className = "";
  }
}

// автозаповнення форми
function autoFillData() {
  submit.disabled = false;
  spanMessage.innerHTML = spanMessage.value;
  const dataEBook = dataFake.fakerBook();
  // console.log("📚 Книга:", dataEBook);

  inputID.value = dataEBook.id;
  inputBookTitle.value = dataEBook["title"];
  inputBookAuthor.value = dataEBook.author;
  selectBookYear.value = dataEBook.year;

  if (dataEBook.ebook) {
    checkboxEbook.checked = true;
    divOpenFile.hidden = false;
    fieldsetEbook.hidden = false;
    labelFileName.innerHTML = dataEBook.ebook.name;
    preInforEBook.innerHTML =
      `Path:  <span style='color: lightgrey'>${dataEBook.ebook.path}</span><br>` +
      `Name:  <span style='color: lightgrey'>${dataEBook.ebook.name}</span><br>` +
      `Size:  <span style='color: lightgrey'>${dataEBook.ebook.size}</span> bites<br>` +
      `Format:  <span style='color: lightgrey'>${dataEBook.ebook.format}</span>`;
    preInforEBook.hidden = false;
    console.log("eBook", dataEBook.ebook.path);
  } else {
    // очистити данні e-book
    clearEBook();
    checkboxEbook.checked = false;
    divOpenFile.hidden = true;
    fieldsetEbook.hidden = true;
    preInforEBook.hidden = true;
  }

  // // перевірка, чи існує вказаний жанр у списку вибору
  // let isGenre = selectBookGenre.querySelector(
  //   `[value="${dataEBook.genre.toLowerCase()}"]`
  // ); // arrayGenre.indexOf(dataBook.genre);
  // console.log(isGenre);
  // if (isGenre == null) {
  //   isGenre = optionBookGenreDetective.cloneNode(false);
  //   isGenre.innerHTML = dataEBook.genre;
  //   isGenre.value = dataEBook.genre.toLocaleLowerCase();
  //   selectBookGenre.append(isGenre);
  // }
  // isGenre.selected = true;

  setGenre(dataEBook.genre);

  // додати дані у Localtorage з ключем no_saved_data
  addNoSavedData();
}

// додати дані у LocalStorage з ключем no_saved_data
function addNoSavedData() {
  const dataBook = createObjectForLocalStorage();
  let data = {};
  data[dataBook.idBook] = dataBook;
  webStorage.setLocalStorage("no_saved_data", data);
}

function createObjectForLocalStorage() {
  return {
    idBook: inputID.value,
    title: inputBookTitle.value,
    author: inputBookAuthor.value,
    year: selectBookYear.value,
    // div E-Book
    eBookChecked: checkboxEbook.checked,
    divOpenFileHidden: divOpenFile.hidden,
    fieldsetEbookHidden: fieldsetEbook.hidden,
    preInforEBookHidden: !preInforEBook.hidden,
    ebookFileName: checkboxEbook.checked ? labelFileName.innerHTML : "",
    infoEBook: checkboxEbook.checked ? preInforEBook.innerHTML : "",
    genre: selectBookGenre.value,
  };
}

function fillData(dataBook) {
  inputID.value = Object.keys(dataBook)[0];
  const data = dataBook[inputID.value];
  checkboxEbook.checked = data.eBookChecked;
  inputBookTitle.value = data.title;
  inputBookAuthor.value = data.author;
  selectBookYear.value = data.year;

  if (checkboxEbook.checked) {
    divOpenFile.hidden = false;
    fieldsetEbook.hidden = false;
    labelFileName.innerHTML = data.ebookFileName;
    preInforEBook.hidden = false;
    preInforEBook.innerHTML = data.infoEBook;
  } else {
    // очистити данні e-book
    clearEBook();
    checkboxEbook.checked = false;
    divOpenFile.hidden = true;
    fieldsetEbook.hidden = true;
    preInforEBook.hidden = true;
  }

  setGenre(data.genre);
}

// додавання категорії жанру у список
function setGenre(genre) {
  // перевірка, чи існує вказаний жанр у списку вибору
  let isGenre = selectBookGenre.querySelector(
    `[value="${genre.toLowerCase()}"]`
  ); // arrayGenre.indexOf(dataBook.genre);
  console.log(isGenre);
  if (isGenre == null) {
    isGenre = optionBookGenreDetective.cloneNode(false);
    isGenre.innerHTML = genre;
    isGenre.value = genre.toLocaleLowerCase();
    selectBookGenre.append(isGenre);
  }
  isGenre.selected = true;
}

// очистити данні e-book
function clearEBook() {
  labelFileName.innerHTML = labelFileName.value;
  preInforEBook.innerHTML = preInforEBook.value;
}

function setID() {
  inputID.value = dataFake.createID();
  const newData = createObjectForLocalStorage();
  const data = webStorage.setLocalStorage("no_saved_data");
}
// let script = document.createElement('script');

// // мы можем загрузить любой скрипт с любого домена
// script.src = "https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.3.0/lodash.js"
// document.head.append(script);

// script.onload = function() {
//   // в скрипте создаётся вспомогательная переменная с именем "_"
//   alert(_.VERSION); // отображает версию библиотеки
//   console.log(_);
// };

// script.onerror = function() {
//   console.log('Error of load: ' + this.src);
// }
