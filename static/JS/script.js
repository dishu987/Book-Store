$('.remove_fav').click(function() {
    console.log("Delete clicked!!")
    var id = $(this).attr("book_id").toString();
    var id1 = 'remove' + id;
    $.ajax({
        type: "GET",
        url: "/removeFav",
        data: {
            book_id: id,
        },
        success: function(data) {
            console.log(data);
            if (data.fav_books_len == 0) {
                document.getElementById("book_len").style.display = "block";
                document.getElementById("custom_pag").style.display = "none";
            }
            document.getElementById(id1).remove();
            document.getElementById("removeFav").innerHTML = data.message;
            document.getElementById("removeFav").style.display = "block";
            setTimeout(() => {
                document.getElementById("removeFav").style.display = "none";
            }, 5000);
        }
    })
});


// For add in fav

$('.add_fav').click(function() {
    console.log("Add clicked!!")
    var title = $(this).attr("title").toString();
    var selling_price = $(this).attr("selling_price").toString();
    var discounted = $(this).attr("discounted").toString();
    var description = $(this).attr("description").toString();
    var brand = $(this).attr("brand").toString();
    var product_image = $(this).attr("product_image").toString();
    var auther = $(this).attr("auther").toString();
    var date = $(this).attr("date").toString();
    var rating_count = $(this).attr("rating_count").toString();
    var rating = $(this).attr("rating").toString();
    $.ajax({
        type: "GET",
        url: "/addFav",
        data: {
            'title': title,
            'selling_price': selling_price,
            'discounted': discounted,
            'description': description,
            'brand': brand,
            'product_image': product_image,
            'auther': auther,
            'date': date,
            'rating_count': rating_count,
            'rating': rating,
        },
        success: function(data) {
            console.log(data);
            let text = data.message + "Book Name:" + title + "." + "Click Ok, for go to saved books.";
            if (confirm(text) == true) {
                window.location.replace('/saved&page=1');
            } else {

            }
            document.getElementById("fav_len").innerHTML = data.fav_len;
        }
    })
});