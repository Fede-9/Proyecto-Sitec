import requests
from typing import Dict, List, Optional 

from dataclasses import dataclass

from patrones.models import CovidInfo


@dataclass
class CovidInfoDto:
    date: Optional[str]
    positive: Optional[int]
    negative: Optional[int]


class CovidGateway:
    _URL_BASE = "https://api.covidtracking.com/"

    def get(self, url, *args, **kwargs):
        url = f'{self._URL_BASE}{url}'
        response = requests.get(url)
        # return response.json()
        return response


class CovidParser:
    def values_parser(slef, data:Dict) -> Optional[dict]:
        return data.json()
    
    def value_parser(self, data:Dict):
        return CovidInfoDto(

            date = data.get('date'),
            positive = data.get('positive'),
            negative = data.get('negative'),

        )


class CovidService:

    def __init__(self):
        self.gateway = CovidGateway()
        self.parser = CovidParser()

    def run(self, url) -> List[CovidInfoDto]:
        response = self.gateway.get(url)
        info_parsed = self.parser.values_parser(response)

        list_dtos = []
        for info in info_parsed:
            dto = self.parser.value_parser(info)
            list_dtos.append(dto)
            CovidInfo.objects.create(
                date = dto.date,
                positive = dto.positive,
                negative = dto.negative,
            )

        return list_dtos