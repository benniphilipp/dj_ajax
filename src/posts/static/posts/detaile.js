console.log('detaile.js');

const backBtn = document.getElementById('back-btn')
const postBox = document.getElementById('post-box')
const updateBtn = document.getElementById('update-btn')
const deleteBtn = document.getElementById('delete-btn')
const alertBox = document.getElementById('alert-box')
const url = window.location.href + 'data/'
const updateUrl = window.location.href + 'update/'
const deleteUrl = window.location.href + 'delete/'
console.log(deleteUrl);
const updateForm = document.getElementById('update-form')
const deleteForm = document.getElementById('delete-form')

const spinnerBox = document.getElementById('spinner-box')

const titelInput = document.getElementById('id_title')
const bodyInput = document.getElementById('id_body')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

backBtn.addEventListener('click', () =>{
    history.back()
});

$.ajax({
    type: 'GET',
    url:  url,
    success: function(response){
        const data = response.data

        if (data.logged_in !== data.author) {
            console.log('deffrent');
        }else{
            updateBtn.classList.remove('not-visible')
            deleteBtn.classList.remove('not-visible')
        }

        const titleEl = document.createElement('h3')
        titleEl.setAttribute('class', 'mt-3')
        titleEl.setAttribute('id', 'title')

        const bodyEl = document.createElement('p')
        bodyEl.setAttribute('class', 'mt-1')
        bodyEl.setAttribute('id', 'body')

        titleEl.textContent = data.title
        bodyEl.textContent = data.body

        postBox.appendChild(titleEl)
        postBox.appendChild(bodyEl)

        titelInput.value = data.title
        bodyInput.value = data.body

        spinnerBox.classList.add('not-visible')
    },
    error: function(error){
        console.log(error);
    }
})

updateForm.addEventListener('submit', e=>{
    e.preventDefault()

    const title = document.getElementById('title')
    const body = document.getElementById('body')

    $.ajax({
        type: 'POST',
        url: updateUrl,
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'title': titelInput.value,
            'body': bodyInput.value,
        },
        success: function(response){
            console.log(response);
            handleAlerts('success', 'post update')
            title.textContent = response.title
            body.textContent = response.body
        },
        error: function(error){
            console.log(error);
        },
    });
})

deleteForm.addEventListener('submit', e=>{
    e.preventDefault()

    $.ajax({
        type: 'POST',
        url: deleteUrl,
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
        },
        success: function(response){
            console.log(response);
            window.location = window.location.origin
            localStorage.setItem('title', titleInput.value)
        },
        error:function(error){
            console.log(error);
        }
    })
})
