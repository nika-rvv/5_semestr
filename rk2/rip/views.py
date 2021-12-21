from django.shortcuts import render
from rip.models import DevTool
from rip.models import Language
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

def index(request):
    tools = DevTool.objects.all()
    languages = Language.objects.all()
    return render(request, "index.html", {"tools": tools, "languages": languages})

def create(request):
    if request.method == "POST":
        dt = DevTool()
        dt.name = request.POST.get("name_tool")
        dt.save()
    return HttpResponseRedirect("/")


def create_language(request):
    if request.method == "POST":
        l = Language()
        l.name = request.POST.get("language")
        l.year = request.POST.get("year")
        l.dev_tool = DevTool.objects.get(name=request.POST.get("name_tool"))
        l.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        language = Language.objects.get(id=id)

        if request.method == "POST":
            language.name = request.POST.get("name")
            language.year = request.POST.get("year")
            language.dev_tool = DevTool.objects.get(name=request.POST.get("lang_dev"))
            language.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"language": language})
    except Language.DoesNotExist:
        return HttpResponseNotFound("<h2>Language not found</h2>")


def edit_devtool(request, id):
    try:
        dev_tool = DevTool.objects.get(id=id)

        if request.method == "POST":
            dev_tool.name_tool = request.POST.get("name_tool")
            dev_tool.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_lib.html", {"dev_tool": dev_tool})
    except DevTool.DoesNotExist:
        return HttpResponseNotFound("<h2>Development tool not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        language = Language.objects.get(id=id)
        language.delete()
        return HttpResponseRedirect("/")
    except Language.DoesNotExist:
        return HttpResponseNotFound("<h2>Language not found</h2>")


def delete_devtool(request, id):
    try:
        dev_tool = DevTool.objects.get(id=id)
        dev_tool.delete()
        return HttpResponseRedirect("/")
    except DevTool.DoesNotExist:
        return HttpResponseNotFound("<h2>Development tool not found</h2>")



