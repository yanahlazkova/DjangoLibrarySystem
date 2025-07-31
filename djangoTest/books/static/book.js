export class Book {
    #id;
    #title;
    #author;
    #year;
    #genre;
    #isAvailable;

    constructor(id, title, author, year, genre, isAvailable) {
        this.#id = id;
        this.#title = title;
        this.#author = author;
        this.#year = year;
        this.#genre = genre;
        this.#isAvailable = isAvailable;
    }

    getInfo() {
        return `ID: ${this.#id}, Назва: ${this.#title}, Автор: ${this.#author}, Рік: ${this.#year}, Жанр: ${this.#genre}, Доступна: ${this.#isAvailable}`
    }

    getId() {
        return this.#id;
    }
    
    getTitle() {
        return this.#title;
    }

    getAuthor() {
        return this.#author;
    }
    
    getYear() {
        return this.#year;
    }
    
    getGenre() {
        return this.#genre;
    }

    getIsAvailable() {
        return this.#isAvailable;
    }

    setIsAvailable() {
        this.#isAvailable = !this.#isAvailable;
        // console.log('isAvailable: ', this.#isAvailable);
        console.log(`Книга (id: ${this.#id}, title: ${this.#title}) ` + (!this.#isAvailable ? 'видана читачу.' : 'повернута до бібліотеки.'));
    }

}

class EBook extends Book{
    #fileSize; // розмір файлу, наприклад, у MB
    #format; // формат (PDF, EPUB тощо)

    constructor(id, title, author, year, genre, isAvailable) {
        super(id, title, author, year, genre, isAvailable);
    }
    
    download(fileSize, format){
        this.#fileSize = fileSize;
        this.#format = format;
        console.log(`Ви завантажили електронну книгу ${super.getTitle()} у форматі ${this.#format} (розмір файлу: ${this.#fileSize} MB)`); 
        return this;
    }

    getInfo(){
        return super.getInfo() + `, розмір файлу: ${this.#fileSize} MB, формат: ${this.#format}`;
    }
}