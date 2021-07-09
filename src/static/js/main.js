$(() => {

    // display modal
    $('#contactForm').on('submit', (event) => {
        event.preventDefault()
        $('.alert-modal').css({
            "display": 'flex',
            "justify-content": "center",
            "align-items": "center",
        })
    })
    
    // share link
    $('#shareBtn').on('click', async () => {
        const shareData = {
            "title": "ContactGain",
            "url": `http://localhost:8000/contact_poll/`,
            "text": "Hey! I just found how i can get 1000 contact to grow my network"
        }
        
        if (navigator.share){
            try{
                await navigator.share(shareData)
                $('#contactForm').submit()
                console.log("shared")
            }
            catch(err){
                console.log("user did not share", err)
            }
        }
        else {
            console.log('sharing is not supported on this browser')
        }
    })

    // close modal
    $('#closeModal').click(() => {
        $('.alert-modal').hide()
    })
})