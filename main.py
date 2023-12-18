from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.events import GoToEvent

app = FastAPI()


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def home() -> list[AnyComponent]:
    """
    Show a table of four users, `/api` is the endpoint the frontend will connect to
    when a user visits `/` to fetch components to render.
    """
    return [
        c.Page(
            components=[
                c.Heading(text='Jake Grella'),
                c.Paragraph(text='Software engineer.'),

                c.LinkList(
                    links=[
                        c.Link(
                            components=[c.Text(text='@jakegrella')],
                            on_click=GoToEvent(url='https://twitter.com/jakegrella'),
                        ),
                        # c.Link(
                        #     components=[c.Text(text='jake@jakegrella.com')],
                        #     on_click=GoToEvent(url='mailto:jake@jakegrella.com'),
                        # ),
                        c.Link(
                            components=[c.Text(text='GitHub')],
                            on_click=GoToEvent(url='https://github.com/jakegrella'),
                        ),
                        c.Link(
                            components=[c.Text(text='LinkedIn')],
                            on_click=GoToEvent(url='https://linkedin.com/in/jakegrella'),
                        )
                  ]),

                c.Heading(text='Experience', level=2),
                c.Paragraph(text='Software Engineer'),
                c.Paragraph(text='@ Northwestern Mutual (July 2021 - Present)'),
                c.Paragraph(text='Modernizing internal applications utilizing a microservice architecture'),
                c.Paragraph(text='Software Developer'),
                c.Paragraph(text='@ Contract (April 2021 - July 2021)'),

                c.Heading(text='Projects', level=2),
                c.Paragraph(text='Cloud Computing Jobs'),

                c.Heading(text='Education', level=2),
            ]
        ),
    ]


@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title='FastUI Demo'))