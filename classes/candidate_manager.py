import json


class CandidateManager:
    def __init__(self, path):
        self.path = path

    def load_candidates_from_json(self):
        """Загружает всех кандидатов"""

        with open(self.path, encoding='utf-8') as file:
            candidates = json.load(file)

        return candidates

    def get_candidate_by_id(self, candidate_id):
        """Возвращает кандидатов по id"""

        candidates = self.load_candidates_from_json()
        for candidate in candidates:
            if candidate_id == candidate["id"]:

                return candidate

    def get_candidates_by_name(self, candidate_name):
        """Возвращает кандидатов по имени"""

        candidates = self.load_candidates_from_json()
        candidates_list = []
        for candidate in candidates:
            candidate_name_lower = candidate_name.lower()
            if candidate_name_lower in candidate["name"].lower():
                candidates_list.append(candidate)

        return candidates_list

    def get_candidates_by_skill(self, skill_name):
        """Возвращает кандидатов по skills"""

        candidates = self.load_candidates_from_json()
        skilled_candidates = []
        for candidate in candidates:
            skill_lower = skill_name.lower()
            if skill_lower in candidate["skills"].lower().split(", "):
                skilled_candidates.append(candidate)

        return skilled_candidates
