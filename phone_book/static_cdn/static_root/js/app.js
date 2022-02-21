function checkSizeAside(num) {
    var asideWidth = document.getElementsByTagName('aside')[num - 1].style.width;
    var sectionWidth = document.getElementsByTagName('section')[0].style.width;
    if (num === 1) {
    } else {
        document.getElementsByTagName('section')[0].style.width = '53%';
        document.getElementsByTagName('aside')[num - 1].style.width = '30%';
        document.getElementsByTagName('aside')[num - 2].style.width = '17%';
    }


}

function checkSizeSction() {
    document.getElementsByTagName('section')[0].style.width = '64%';
    document.getElementsByTagName('aside')[0].style.width = '17%';
    document.getElementsByTagName('aside')[1].style.width = '19%';


}

function search() {
    alert(getElementById("search").innerHTML);
}

function addFrame() {
    let addFrame = document.getElementsByName("add")[0]
    let searchFrame = document.getElementsByName("search")[0]

    // if (!searchFrame.hidden) {
    //     searchFrame.hidden = false;
    //     console.log(!searchFrame.hidden);

    // }

    if (addFrame.hidden) {
        addFrame.hidden = false
    } else {
        addFrame.hidden = true
    }

}

function searchFrame() {
    var addFrame = document.getElementsByName("add")[0]
    var dialog = document.getElementsByTagName("dialog")[0]

    console.log(dialog.open)
    if (!dialog.open) {
        dialog.show();

    } else {
        dialog.close();

    }
}

var selectState = false;
var listItem = []

function selectItems() {
    selectState = !selectState;
    if (selectState) {
        document.getElementsByTagName('section')[0].style.backgroundColor = 'lightBlue';
    } else {
        document.getElementsByTagName('section')[0].style.backgroundColor = 'blue';
        childrenOfSection = document.getElementsByTagName('section')[0].children
        for (const child of childrenOfSection) {
            child.children[0].checked = false;
            child.style.backgroundColor = ''
        }
        listItem = []
        // for (const child in childrenOfSection) {
        //     console.log(child)
        //
        // }

    }


}

function selectItem(id) {
    const element = document.getElementById(id)
    if (selectState) {
        divComputedStyle = getComputedStyle(element)
        if (divComputedStyle.backgroundColor == 'rgb(0, 0, 255)') {
            element.children[0].checked = false
            element.style.backgroundColor = '';
            const index = listItem.indexOf(element.id);
            if (index > -1) {
                listItem.splice(index, 1); // 2nd parameter means remove one item only
            }
        } else {
            listItem.push(element.id)
            element.children[0].checked = true
            element.style.backgroundColor = 'blue';
        }
        console.log(listItem)

    } else if (!selectState) {
        const elementInAside = document.getElementsByTagName('aside')[1].children[0].children
        elementInAside[0].src = element.children[0].src
        for (let i = 0; i < elementInAside.length; i++) {

            elementInAside[i].innerHTML = element.children[i].innerHTML

        }

    }


}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function deleteItem() {
    str = ``
    // var search = location.search.substring(1);
    for (const pk of listItem) {
        str = `PK=${pk}&` + str
    }
    var csrftoken = getCookie('csrftoken');
    const request = new XMLHttpRequest()
    request.open('POST', '/delete-contact')
    request.setRequestHeader('X-CSRFToken', csrftoken)
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    if (request.readyState == 4 && request.status == 200){
        request.responseText;
        document.location.reload()
    }
    request.send(str);



}

function addFile() {
    var dialog = document.getElementsByTagName("dialog")[1]

    console.log(dialog.open)
    if (!dialog.open) {
        dialog.show();

    } else {
        dialog.close();

    }
}