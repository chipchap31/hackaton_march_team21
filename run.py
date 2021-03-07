from app import create_app
import os

app = create_app()


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    port=int(os.environ.get('PORT') or 5000),
    debug=False
    )

