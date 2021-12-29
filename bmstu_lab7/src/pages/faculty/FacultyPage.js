import {MainPage} from "../main/MainPage.js";
import {FacultyComponent} from "../../components/faculty/FacultyComponent.js";
import {BackButtonComponent} from "../../components/back-button/BackButton.js";
import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";

export class FacultyPage {
    constructor(parent, id) {
        this.parent = parent
        this.id = id
    }

    async getData() {
        return ajax.get(urls.faculty(this.id))
    }

    clickBack() {
        const mainPage = new MainPage(this.parent)
        mainPage.render()
    }

    get page() {
        return document.getElementById('faculty-page')
    }

    getHTML() {
        return (
            `
                <div id="faculty-page">
                </div>
            `
        )
    }

    async render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)

        const backButton = new BackButtonComponent(this.page)
        backButton.render(this.clickBack.bind(this))

        const data = this.getData()
        const faculty = new FacultyComponent(this.page)
        faculty.render(data.data)
    }
}