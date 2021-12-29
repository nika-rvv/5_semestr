import {FacultyPage} from "../faculty/FacultyPage.js";
import {FacultyCardComponent} from "../../components/faculty-card/FacultyCardComponent.js";
import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";

export class MainPage {
    constructor(parent) {
        this.parent = parent;
    }

    async getData() {
        return ajax.get(urls.faculties())
    }

    clickCard(e) {
        const cardId = e.target.dataset.id

        const facultyPage = new FacultyPage(this.parent, cardId)
        facultyPage.render()
    }

    get page() {
        return document.getElementById('main-page')
    }

    getHTML() {
        return (
            `
                <div id="main-page" class="d-flex flex-wrap"><div/>
            `
        )
    }

    async render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)

        const data = await this.getData()
        data.data.forEach((item) => {
            const facultyCard = new FacultyCardComponent(this.page)
            facultyCard.render(item, this.clickCard.bind(this))
        })
    }
}