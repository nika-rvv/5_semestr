class Urls {
    constructor() {
        this.url = 'http://127.0.0.1:8080/';
    }

    faculties() {
        return `${this.url}faculties/`
    }

    faculty(id) {
        return `${this.url}faculties/${id}/`
    }
}

export const urls = new Urls()