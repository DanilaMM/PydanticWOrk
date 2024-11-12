from pydantic import BaseModel, Field, ConfigDict


class ScoreGroup(BaseModel):
    avg_score: float = Field(alias='avgMark')
    max_score: float = Field(alias='maxMark')
    min_score: float = Field(alias='minMark')
    model_config = ConfigDict(populate_by_name=True)


group1 = ScoreGroup(avg_score=3.15, min_score=2.20, max_score=4.90)

to_json = group1.json()
print(to_json)
