import React, { useState } from 'react';
import { Container, Group, Burger } from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';
import { MantineLogo } from '@mantine/ds';
import classes from './HeaderSimple.module.css';

const links = [
  { link: '/about', label: 'Features' },
  { link: '/pricing', label: 'Pricing' },
  { link: '/learn', label: 'Learn' },
  { link: '/community', label: 'Community' },
];

class HeaderSimple extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      opened: false,
      active: links[0].link,
    };
  }

  toggle = () => {
    this.setState((prevState) => ({ opened: !prevState.opened }));
  };

  handleClick = (event, link) => {
    event.preventDefault();
    this.setState({ active: link });
  };

  render() {
    const { opened, active } = this.state;

    const items = links.map((link) => (
      <a
        key={link.label}
        href={link.link}
        className={classes.link}
        data-active={active === link.link || undefined}
        onClick={(event) => this.handleClick(event, link.link)}
      >
        {link.label}
      </a>
    ));

    return (
      <header className={classes.header}>
        <Container size="md" className={classes.inner}>
          <MantineLogo size={28} />
          <Group gap={5} visibleFrom="xs">
            {items}
          </Group>

          <Burger opened={opened} onClick={this.toggle} hiddenFrom="xs" size="sm" />
        </Container>
      </header>
    );
  }
}

export default HeaderSimple;
