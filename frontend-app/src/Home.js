import React, { Component } from 'react';
import Table from "./Table";
import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';


class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      jsonData: null,
    };
  }

  componentDidMount() {
    fetch('http://localhost:8000/api/get/strings')
      .then(response => response.json())
      .then(data => {
        console.log(data);
        this.setState({ jsonData: data });
      })
      .catch(error => {
        console.error('Ошибка при получении данных:', error);
      });
  }

  render() {
    const { jsonData } = this.state;
    const columns = [
      {
        dataField: 'number',
        text: '№',
        sort: true,
      },
      {
        dataField: 'track_title',
        text: 'Название трека',
        sort: true,
      },
      {
        dataField: 'performer_name',
        text: 'Исполнитель',
        sort: true,
      },
      {
        dataField: 'genre_title',
        text: 'Жанр',
        sort: true,
      },
      {
        dataField: 'duration',
        text: 'Длительность',
        sort: true,
      }
    ];

    return (
      <div>
        {jsonData ? (
          <div>
            {/* Вывод данных на странице */}
            {jsonData.map(item => (
              <Table key={item.disk} data={item.strings} columns={columns} name={item.disk} />
            ))}
          </div>
        ) : (
          <p>Загрузка данных...</p>
        )}
      </div>
    );
  }
}

export default Home;
