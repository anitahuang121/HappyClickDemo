# HappyClickService
目前架設在 heroku server 上，可以直接用postman之類的測試
## 使用方式
- 查詢預約接種名單 url : https://happyclick-healthcenter.herokuapp.com/SearchFormData
- 上傳接種資料 url : https://happyclick-healthcenter.herokuapp.com/UpdateVaccinated
# Health center API
### SearchFormData 查詢預約接種名單 (POST)
- Input : 
    - date (string, ex. {"date":"2021/08/12"})
- Output : 
    - 有資料 
        - list[{form_id(integer), vaccine_type(string), ID(integer), Name(string)}, .....]
    - 沒資料 
        - {'msg' : 'No FormData data!'}
### UpdateVaccinated 上傳接種資料 (POST)
- Input : 
    - {form_id(integer), ID(integer), Name(string)}
- Output : 
    - {'msg' : 'Update Vaccinated successful!'}
