$(document).ready(() => {

    // method to make HTTPRequest 
    const ajaxRequest = (payload, then, err) => {
        $.ajax({
            type: payload.type,
            url: payload.url,
            dataType: "json",

            success: (data) => {
                then(data);
            },
            error: (error) => {
                err(error);
            },
        });
    };

    const print = (value) => {
        console.log(value);
    };



    // post liking functionality 

    like_btn = document.querySelectorAll(
        "#home-posts ul li.post-container .bottom .likes .wrap"
    );

    like_btn.forEach((btn) => {
        btn.addEventListener("click", (e) => {
            e.preventDefault();

            let show_like = btn.parentElement.querySelector("p");
            let post_id = btn.getAttribute("data-post-id");
            let like_img = btn.querySelector("img");

            let like_btn_success = (data) => {
                show_like.innerText = `${data.likes} likes`;
                if (data.status == "already liked") {
                    like_img.src = "/static/images/like.png";
                } else {
                    like_img.src = "/static/images/liked.png";
                }
            };

            let like_btn_error = (error) => {
                console.log(error);
            };
            let like_btn_payload = {
                type: "get",
                url: `/posts/${post_id}/like/`,
            };

            ajaxRequest(like_btn_payload, like_btn_success, like_btn_error);
        });
    });



    // profile delete functionality 

    let delete_profile = document.getElementById("delete_profile");
    if (delete_profile) {
        id = delete_profile.getAttribute("data-id");
        delete_profile.addEventListener("click", (e) => {
            e.preventDefault();
            Swal.fire({
                title: "Are you sure?",
                text: "You won't be able to revert this!",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Yes, delete it!",
            }).then((result) => {
                if (result.isConfirmed) {
                    let delete_profile_success = (data) => {
                        console.log(data);
                    };
                    let delete_profile_error = (err) => {
                        console.log(error);
                    };
                    let delete_profile_payload = {
                        type: "get",
                        url: `/users/${id}/delete/`,
                    };

                    ajaxRequest(
                        delete_profile_payload,
                        delete_profile_success,
                        delete_profile_error
                    );

                    Swal.fire(
                        "Deleted!",
                        "Your file has been deleted.",
                        "success"
                    ).then(() => {
                        console.log("deleted successfully");
                        window.location.assign("/");
                    });
                }
            });
        });
    }


    // post delete functionality 

    let delete_post = document.getElementById("delete-post");
    if (delete_post) {
        delete_post.addEventListener("click", (e) => {
            e.preventDefault();

            let url = delete_post.getAttribute("href");
            print(url);

            Swal.fire({
                title: "Are you sure?",
                text: "You won't be able to revert this!",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Yes, delete it!",
            })
            .then((result) => {
                if (result.isConfirmed) {
                    let delete_post_success = (data) => {
                        console.log(data);
                    };

                    let delete_post_error = (error) => {
                        console.log(error);
                    };

                    let delete_post_payload = { type: "get", url: url };

                    ajaxRequest(
                        delete_post_payload,
                        delete_post_success,
                        delete_post_error
                    );

                    Swal.fire(
                        "Deleted!",
                        "Your file has been deleted.",
                        "success"
                    ).then(() => {
                        console.log("deleted successfully");
                        window.location.assign("/");
                    });
                }
            });
        });
    }


    // follow and unfollow functionality 

    let follow_btn = document.getElementById("follow")
    let followers_count = document.querySelector('.followers-count')
    if (follow_btn) {
        follow_btn.addEventListener("click",(e)=>{
            e.preventDefault();
            let follow_success = (data) => {
                $('.followers-count').html(data.followers)
                // followers_count.innerHTML(data.follower)
                if (data.title == 'success') {
                    if (follow_btn.innerText == 'unfollow') {
                        follow_btn.innerText = 'follow';

                    }else if(follow_btn.innerText == 'follow'){
                        follow_btn.innerText = 'unfollow';
                    }
                }
            };

            let follow_error = (error) => {
                console.log(error);
            };

            let follow_payload = { type: "get", url: 'follow/' };
            if (follow_btn.innerText == 'unfollow') {
                follow_payload.url = 'unfollow/'
            }

            ajaxRequest(
                follow_payload,
                follow_success,
                follow_error
            );
        })
    }








});
