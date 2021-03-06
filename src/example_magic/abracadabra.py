from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)
from IPython.core.display import display, HTML
from IPython.display import IFrame

@magics_class
class Abracadabra(Magics):

    @line_magic
    def youre_a_magic_harry(self, line):
        return ":D"

    @line_magic
    def an_iframe(self, line):
        iframe = IFrame(src='https://s3.amazonaws.com/duhaime/blog/visualizations/isolation-forests.html', width=700, height=600)
        return iframe

    @line_magic
    def my_iframe(self, line):
        return IFrame(src='./index.html', width=700, height=600)

    @line_magic
    def my_iframe_except_its_actually_external(self, line):
        return IFrame(src='https://raw.githubusercontent.com/Llewi/AnIPythonExtension/main/src/example_magic/index.html', width=700, height=600)

    @line_magic
    def all_in_one_line(self, line):
        return display(HTML(
            """
<head>
    <title>the good stuff</title>
    <script src="https://unpkg.com/react@18/umd/react.development.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js" crossorigin></script>
    <script>
        'use strict';

        console.log('anything?');

        const e = React.createElement;

        class LikeButton extends React.Component {
            constructor(props) {
                super(props);
                this.state = { liked: false };
            }

            render() {
                if (this.state.liked) {
                    return 'You liked this.';
                }

                return e(
                    'button',
                    { onClick: () => this.setState({ liked: true }) },
                    'Like'
                );
            }
        }

        const domContainer = document.querySelector('#like_button_container');
        const root = ReactDOM.createRoot(domContainer);
        root.render(e(LikeButton));

    </script>
</head>

<body>
    <h1>Hello, world.</h1>
    <div id="like_button_container"></div>
</body>
            """
        ))

    @line_magic
    def it_is_html(self, line):
        return display(HTML('<h1>Hello, world!</h1>'))

    @line_magic
    def abra(self, line):
        return line + "!"

    @cell_magic
    def cadabra(self, line, cell):
        return line, cell

    def vanilla_method(self):
        return "literally no flavour"
