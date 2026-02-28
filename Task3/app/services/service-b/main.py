from fastapi import FastAPI
from opentelemetry import trace  # pyright: ignore[reportMissingImports]
from opentelemetry.exporter.jaeger.thrift import JaegerExporter  # pyright: ignore[reportMissingImports]
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor  # pyright: ignore[reportMissingImports]
from opentelemetry.sdk.resources import Resource, SERVICE_NAME  # pyright: ignore[reportMissingImports]
from opentelemetry.sdk.trace import TracerProvider  # pyright: ignore[reportMissingImports]
from opentelemetry.sdk.trace.export import BatchSpanProcessor  # pyright: ignore[reportMissingImports]


resource = Resource(attributes={
    SERVICE_NAME: "service-b"
})

provider = TracerProvider(resource=resource)
jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)
provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

app = FastAPI()
FastAPIInstrumentor.instrument_app(app)

@app.get("/get-shopping-cart-items")
def shopping_cart_items() -> list[dict]:
    return [
        {
            'id': 1,
            'name': 'Item 1',
            'price': 100,
            'quantity': 1
        },
        {
            'id': 2,
            'name': 'Item 2',
            'price': 200,
            'quantity': 2
        }
    ]