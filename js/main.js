function generateCards() {
    $(document).ready(function () {
        $.getJSON("parade.json", function (data) {
            for (i = 0; i < data.floats.length; i++) {
                $("#parade-cards").append(`
                <div class="carousel-item">
                    <div class="d-flex align-items-center justify-content-center min-vh-100">
                        <div class="card" style="width: 60%;">
                            <img src="${data.floats[i].image}" class="card-img-top" alt="${data.floats[i].name}'s image">
                            <div class="card-body">
                                <p class="card-text text-center">${data.floats[i].name} from ${data.floats[i].country} says: ${data.floats[i].message}</p>
                            </div>
                        </div>
                    </div>
                </div>
            `)
        }        
        }).fail(function () {
            console.log("An error has occurred.");
        });
    });
}