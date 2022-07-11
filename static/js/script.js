$(document).ready(() => {
    like_btn = document.querySelectorAll('#home-posts ul li.post-container .bottom .likes .wrap')
    console.log(like_btn);
    
    like_btn.forEach(btn => {
        btn.addEventListener('click',(e) => {
            e.preventDefault();

            let show_like = btn.parentElement.querySelector('p')
            let post_id = btn.getAttribute('data-post-id')
            let like_img = btn.querySelector('img')
            console.log(like_img.src);
            $.ajax({
                type:'get',
                url:`/posts/${post_id}/like/`,
                dataType:'json',
    
                success : (data)=>{
                    show_like.innerText = `${data.likes} likes`
                    if (data.status == 'already liked'){
                        like_img.src = '/static/images/like.png'
                    }else{
                        like_img.src = '/static/images/liked.png'
                    }

                    
                    // Swal.fire({
                    //     icon: data.status,
                    //     title: data.title,
                    //     text: data.message
                    //   })
                    //   if(data.status == 'success'){
                    //         this.reset();
                    //   }
                },
                error : (error)=>{
                    console.log(error);
                },
            })
        })
    });









    $(document).on("submit", "form.subscribe", function (e) {
        e.preventDefault();
        var $this = $(this);

        var url = $this.attr("action");
        var method = $this.attr("method");

        $.ajax({
            type:'get',
            url:'/posts/post_id/like/',
            dataType:'json',

            success : (data)=>{
                Swal.fire({
                    icon: data.status,
                    title: data.title,
                    text: data.message
                  })
                  if(data.status == 'success'){
                        this.reset();
                  }
            },
            error : (error)=>{
                console.log(error);
            },
        })
    });
});