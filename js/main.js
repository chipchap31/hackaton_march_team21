function generateCards() {
    $("#parade-cards").append(`
        <div class="carousel-item">
            <div class="d-flex align-items-center justify-content-center min-vh-100">
                <div class="card" style="width: 60%;">
                    <img src="images/flower.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                        <p class="card-text text-center">John Smith from America says: How did I get here?</p>
                    </div>
                </div>
            </div>
        </div>
    `)}