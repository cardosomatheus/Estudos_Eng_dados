import json
import pendulum

from airflow.sdk import dag, task



@dag(
    schedule=None,
    description="Airflow 3 with decorators",
    start_date=pendulum.datetime(2025,1,1, tz="utc"),  
    catchup=False,
    tags=["Pipline", "etl", "Example"]
)


def tutorial_task_airflow_api() -> None:
    """
        ### TaskFlow API Tutorial Documentation
        This is a simple data pipeline example which demonstrates the use of
        the TaskFlow API using three simple tasks for Extract, Transform, and Load.
        Documentation that goes along with the Airflow TaskFlow API tutorial is
        located
        [here](https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html)
    """

    @task(retries=2)
    def extract()-> json:
        """
            #### Extract task
            A simple Extract task to get data ready for the rest of the data
            pipeline. In this case, getting data is simulated by reading from a
            hardcoded JSON string.
        """

        data_string = '{"1001":301.59, "1002":501.59, "1003":701.59, "1004":1001.42,  "1005":10.90}'
        order_data_dict = json.loads(data_string)
        return order_data_dict
    

    @task(multiple_outputs=True)
    def transform(order_data_dict: dict) -> dict:
        """
            #### Transform task
            A simple Transform task which takes in the collection of order data and
            computes the total order value.
        """
        quantity_value = 0
        total_order_value = 0
        for value in order_data_dict.values():
            total_order_value += value
            quantity_value += 1

        return {"total_order_value": total_order_value,
                "Quantity_order":quantity_value}


    @task()
    def load(total_order_value: float):
        """
            #### Load task
            A simple Load task which takes in the result of the Transform task and
            instead of saving it to end user review, just prints it out.
            """

        print(f"Total order value is: {total_order_value:.2f}")



    @task()
    def median_analysis(order_data_dict_transformed: dict) -> float:
        """### BI ANALYSIS
           This process will seek the average of the values the number of orders
        """

        median =  order_data_dict_transformed.get("total_order_value")/order_data_dict_transformed.get("Quantity_order")
        
        print(f"MEDIAN: {median}")


    order_data = extract()
    order_summary = transform(order_data)
    load(order_summary["total_order_value"])
    median_analysis(order_summary)




tutorial_task_airflow_api()
