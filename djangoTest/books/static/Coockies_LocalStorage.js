// COOKIES

// встановлення кукі (зберігає встановлений колір тексту)
export function setCookies(e, cname = "text_color", cvalue = "green") {
  // const
  if (!e) {
    document.cookie =
      cname + "=" + (!document.cookie.length ? cvalue : getCookiesColor(cname));
  } else document.cookie = cname + "=" + e.target.value;
}

// отримання кукі
export function getCookiesColor(cname) {
  const arrayCookies = document.cookie.split(";"); // створимо масив
  if (arrayCookies) {
    const cookie = arrayCookies.filter(
      (value) => value.split("=")[0].trim() == cname
    );
    //   console.log(cookie[0].split('=')[1]);
    console.log("cookie", cookie);
    return cookie.length ? cookie[0].split("=")[1] : NaN;
  }
  return NaN;
}

// Local Storage

export function setLocalStorage(key, data) {
  return new Promise((resolve, reject) => {
    try {
      localStorage.setItem(key, JSON.stringify(data));
      resolve("Додано");
    } catch (error) {
      reject("Помилка при збереженні даних у " + key);
    }
  });
}

export function getLocalStorage(key) {
  return JSON.parse(localStorage.getItem(key));
}

export function removeLocalStorage(key) {
  return new Promise((resolve, reject) => {
    try {
      localStorage.removeItem(key);
      resolve(`Видалено ${key}`);
    } catch (error) {
      reject("Error removing..");
    }
  });
}
