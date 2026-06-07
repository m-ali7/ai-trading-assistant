import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="ask")
def ask(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Trading Assistant request received")

    try:
        from src.data_loader import load_trading_metrics
        from src.chat_assistant import answer_trading_question

        req_body = req.get_json()

        question = req_body.get("question")
        market = req_body.get("market", "UK")
        category = req_body.get("category", "Dresses")

        if not question:
            return func.HttpResponse(
                json.dumps({"error": "Question is required"}),
                status_code=400,
                mimetype="application/json"
            )

        df = load_trading_metrics("data/trading_metrics.csv")

        answer = answer_trading_question(
            df=df,
            market=market,
            category=category,
            question=question
        )

        return func.HttpResponse(
            json.dumps({
                "question": question,
                "market": market,
                "category": category,
                "answer": answer
            }),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.exception("Trading Assistant failed")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
@app.route(route="monday-brief")
def monday_brief(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Monday Brief request received")

    try:
        from src.data_loader import load_trading_metrics
        from src.manager_brief_generator import generate_manager_brief

        req_body = req.get_json()
        manager_email = req_body.get("manager_email", "sarah.manager@example.com")

        df = load_trading_metrics("data/trading_metrics.csv")
        brief = generate_manager_brief(df, manager_email)

        return func.HttpResponse(
            json.dumps({
                "manager_email": manager_email,
                "brief": brief
            }),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.exception("Monday Brief failed")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
